from django.db import models

# Create your models here.
class Pricing(models.Model):
    numberToppings = models.IntegerField()
    small_price = models.DecimalField(max_digits=5, decimal_places=2)
    large_price = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.BooleanField()

    def __str__(self):
        return "Number of toppings: " + str(self.numberToppings)

class Topping(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return str(self.topping)

class Order(models.Model):
    size = models.IntegerField()
    numberToppings = models.IntegerField()
    type = models.BooleanField()
    toppings = models.ManyToManyField(Topping, blank=True, related_name="orders")

    def __str__(self):
        return "Order: " + str(self.size)
