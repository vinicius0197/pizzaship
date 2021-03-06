from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("registration", views.registration, name="registration"),
    path("shop", views.shop, name="shop"),
    path("cart", views.cart, name="cart"),
    path("order", views.order, name='order'),
    path("view_cart", views.view_cart, name="view_cart"),
    path("send_order", views.send_order, name="send_order")
]
