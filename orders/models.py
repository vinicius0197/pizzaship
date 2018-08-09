from django.db import models

# Create your models here.
class Pricing(models.Model):
    # Define types of toppings for pizza
    CHEESE = 'Cheese'
    T1 = '1 Topping'
    T2 = '2 Toppings'
    T3 = '3 Toppings'
    T4 = 'Special'

    TOPPING_TYPES = (
        (CHEESE, 'Cheese'),
        (T1, '1 topping'),
        (T2, '2 toppings'),
        (T3, '3 toppings'),
        (T4, 'Special'),
    )
    number_toppings = models.CharField(max_length=12,
                                        choices=TOPPING_TYPES,
                                        default=CHEESE)
    small_price = models.DecimalField(max_digits=5, decimal_places=2)
    large_price = models.DecimalField(max_digits=5, decimal_places=2)

    REGULAR = 'R'
    SICILIAN = 'S'
    PIZZA_TYPES = (
        (REGULAR, 'Regular'),
        (SICILIAN, 'Sicilian'),
    )
    type = models.CharField(max_length=2,
                            choices=PIZZA_TYPES,
                            default=REGULAR)

class Topping(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return str(self.topping)

class Order(models.Model):
    CHEESE = 'CHEESE'
    T1 = '1'
    T2 = '2'
    T3 = '3'
    T4 = 'SPECIAL'

    TOPPING_TYPES = (
        (CHEESE, 'Cheese'),
        (T1, '1 topping'),
        (T2, '2 toppings'),
        (T3, '3 toppings'),
        (T4, 'Special'),
    )
    number_toppings = models.CharField(max_length=10,
                                        choices=TOPPING_TYPES,
                                        default=CHEESE)
    LARGE = 'L'
    SMALL = 'S'
    SIZE_OPTIONS = (
        (LARGE, 'Large'),
        (SMALL, 'Small'),
    )

    size = models.CharField(max_length=1,
                            choices=SIZE_OPTIONS,
                            default=SMALL)
    REGULAR = 'R'
    SICILIAN = 'S'
    PIZZA_TYPES = (
        (REGULAR, 'Regular'),
        (SICILIAN, 'Sicilian'),
    )
    type = models.CharField(max_length=2,
                            choices=PIZZA_TYPES,
                            default='Regular')
    toppings = models.ManyToManyField(Topping, blank=True, related_name="orders")
    final_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return "Order: " + str(self.size)
