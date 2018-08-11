from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from orders.models import Pricing, Topping, Order, Cart

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
            # Check if user already has items in cart
            user = User.objects.get(username=request.user)
            cart = Cart.objects.filter(user=user.username)
            if cart.exists():
                return HttpResponse("You already have items in your cart")
            # Queries for pricing data
            pricing = Pricing.objects.all()

            size = form.cleaned_data["size"]
            subs = form.cleaned_data["subs"]
            type = form.cleaned_data["type"]

            try:
                prices_for_subs = Pricing.objects.get(number_toppings=subs, type=type)
            except Pricing.DoesNotExist:
                return HttpResponse('Pricing data not found')
            if size == 'small':
                price = prices_for_subs.small_price
            elif size == 'large':
                price = prices_for_subs.large_price
            
            which_toppings = form.cleaned_data["which_toppings"]
            
            # Creates cart object
            cart = Cart.objects.create(
                number_toppings = subs,
                type = type,
                size = size,
                price = price,
                user = user.username
            )

            query_list = []
            for item in which_toppings:
                query_list.append(Topping.objects.get(topping=item))
            
            cart.toppings.add(*query_list)
            cart.save()
            return HttpResponseRedirect(reverse("view_cart"))
        else:
            return HttpResponse("Invalid form")
    else:
        return HttpResponseRedirect(reverse("shop"))

def view_cart(request):
    user = User.objects.get(username=request.user)
    cart = Cart.objects.filter(user=user.username)
    context = {
        "cart": cart
    }
    return render(request, "cart.html", context)

def send_order(request):
    user = User.objects.get(username=request.user)
    cart = Cart.objects.get(user=user.username)

    # Create order object
    order = Order.objects.create(
        number_toppings = cart.number_toppings,
        size = cart.size,
        type = cart.type,
        user = cart.user,
        final_price = cart.price
    )
    for topping in cart.toppings.all():
        order.toppings.add(topping)
    order.save()
    
    # Clean user cart
    cart.delete()

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