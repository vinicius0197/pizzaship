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

    PIZZA_TYPES = (
        ('R', 'Regular'),
        ('S', 'Sicilian'),
    )
    type = models.CharField(max_length=2,
                            choices=PIZZA_TYPES,
                            default='regular')

class Topping(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return str(self.topping)

class Order(models.Model):
    TOPPING_TYPES = (
        ('Cheese', 'Cheese'),
        ('1 Topping', '1 topping'),
        ('2 Toppings', '2 toppings'),
        ('3 Toppings', '3 toppings'),
        ('Special', 'Special'),
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
        ('R', 'Regular'),
        ('S', 'Sicilian'),
    )
    type = models.CharField(max_length=10,
                            choices=PIZZA_TYPES,
                            default='Regular')
    toppings = models.ManyToManyField(Topping, blank=True, related_name="orders")
    
    user = models.CharField(max_length=64, default='user')

    final_price = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return "Order: " + str(self.size)

class Cart(models.Model):
    number_toppings = models.CharField(max_length=10,
                                        default='Cheese')
    size = models.CharField(max_length=10, default='Small')
    type = models.CharField(max_length=10, default='Regular')
    toppings = models.ManyToManyField(Topping, blank=True)
    user = models.CharField(max_length=64, default='none')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
