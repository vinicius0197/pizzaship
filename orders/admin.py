from django.contrib import admin
from .models import Pricing, Topping, Order, Cart

# Register your models here.
admin.site.register(Pricing)
admin.site.register(Topping)
admin.site.register(Order)
admin.site.register(Cart)