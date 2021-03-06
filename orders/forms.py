from django import forms
from orders.models import Pricing, Topping

class OrderForm(forms.Form):
    size_choices = (
        ('small', 'Small'),
        ('large', 'Large'),
    )
    size = forms.ChoiceField(label='Size',
                            choices=size_choices)

    topping_types = (
        ('Cheese', 'Cheese'),
        ('1 Topping', '1 topping'),
        ('2 Toppings', '2 toppings'),
        ('3 Toppings', '3 toppings'),
        ('Special', 'Special'),
    )

    subs = forms.ChoiceField(label='Toppings',
                            choices=topping_types)

    type_options = (
        ('R', 'Regular'),
        ('S', 'Sicilian'),
    )

    type = forms.ChoiceField(label='Type', choices=type_options)

    # Get data from Toppings model and convert into a tuple
    topping_list = []
    toppings = Topping.objects.all()
    for topping in toppings:
        item = (topping.topping, topping.topping)
        topping_list.append(item)
    toppings_options = tuple(topping_list)
    
    # Create form option for showing toppings to user
    which_toppings = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, 
                                                choices=toppings_options)
