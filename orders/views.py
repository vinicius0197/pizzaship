from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from orders.models import Pricing, Topping, Order

from .forms import OrderForm

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    context = {
        "user": request.user
    }
    return HttpResponseRedirect(reverse("shop"))

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("shop"))
    else:
        return render(request, "login.html", {"message": "Invalid Credentials"})

def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})

def registration(request):
    """ Handles user registration """
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]

        user = User.objects.create_user(username, email, password)
        user.save()

        # Login user after registration
        user = authenticate(request, username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(reverse("shop"))
    else:
        return render(request, "registration.html", {"message": None})

def shop(request):
    """ Renders shopping information to user """
    if request.method == 'GET':
        form = OrderForm()
        context = {
            "form": form
        }

        return render(request, "shop.html", context)

def cart(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            pricing = Pricing.objects.all()

            size = form.cleaned_data["size"]
            subs = form.cleaned_data["subs"]
            type = form.cleaned_data["type"]

            prices_for_subs = Pricing.objects.get(number_toppings=subs)
            if size == 'small':
                price = prices_for_subs.small_price
            elif size == 'large':
                price = prices_for_subs.large_price
            
            which_toppings = form.cleaned_data["which_toppings"]
            user = User.objects.get(username=request.user)
            order = Order.objects.create(
                number_toppings = subs,
                type = type,
                size = size,
                final_price = price,
                user = user.username
            )

            query_list = []
            for item in which_toppings:
                query_list.append(Topping.objects.get(topping=item))
            
            order.toppings.add(*query_list)
            order.save()
            return HttpResponseRedirect(reverse("shop"))
        else:
            return HttpResponse("Invalid form")
    else:
        return HttpResponseRedirect(reverse("shop"))

def order(request):
    if request.method == 'GET':
        if request.user.is_superuser:
            # Query database for all orders
            orders = Order.objects.all()
            context = {
                "order_data": orders
            }
            return render(request, "orders.html", context)
    else:
        return HttpResponse('Not allowed')