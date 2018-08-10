from django.db import models

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
    TOPPING_TYPES = (
        ('0', 'Cheese'),
        ('1', '1 topping'),
        ('2', '2 toppings'),
        ('3', '3 toppings'),
        ('4', 'Special'),
    )
    number_toppings = models.CharField(max_length=10,
                                        choices=TOPPING_TYPES,
                                        default='Cheese')
    SIZE_OPTIONS = (
        ('large', 'Large'),
        ('small', 'Small'),
    )

    size = models.CharField(max_length=10,
                            choices=SIZE_OPTIONS,
                            default='Small')
    PIZZA_TYPES = (
        ('regular', 'Regular'),
        ('sicilian', 'Sicilian'),
    )
    type = models.CharField(max_length=10,
                            choices=PIZZA_TYPES,
                            default='Regular')
    toppings = models.ManyToManyField(Topping, blank=True, related_name="orders")
    
    final_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return "Order: " + str(self.size)
