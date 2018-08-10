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

def order(request):
    # TODO handle order and create an 'order' object in database
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # handle order fields here https://docs.djangoproject.com/en/dev/topics/forms/#using-a-form-in-a-view
            size = form.cleaned_data["size"]
            subs = form.cleaned_data["subs"]
            type = form.cleaned_data["type"]
            which_toppings = form.cleaned_data["which_toppings"]
            
            order = Order.objects.create(
                number_toppings = subs,
                type = type,
                size = size
            )
            choosen_toppings = Topping.objects.get(topping=which_toppings[0])
            order.toppings.add(choosen_toppings)
            order.save()

            return HttpResponseRedirect(reverse("shop"))
    else:
        return HttpResponseRedirect(reverse("shop"))