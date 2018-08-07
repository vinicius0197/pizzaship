from django.db import models

# Create your models here.
class Pricing(models.Model):
    topping = models.IntegerField()
    small_price = models.DecimalField(max_digits=5, decimal_places=2)
    large_price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.BooleanField()
