from django.contrib import admin
from .models import Pricing, Topping, Order

# Register your models here.
admin.site.register(Pricing)
admin.site.register(Topping)
admin.site.register(Order)
