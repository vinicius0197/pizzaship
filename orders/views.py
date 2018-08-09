from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse

from orders.models import Pricing, Topping

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"message": None})
    context = {
        "user": request.user
    }
    # return render(request, "shop.html", context)
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
    toppings = Topping.objects.all()

    context = {
        "toppings": toppings
    }

    return render(request, "shop.html", context)

def order(request):
    # TODO
    pass