# Generated by Django 2.0.3 on 2018-08-08 00:36

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('orders', '0002_auto_20180807_2328'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
    ]
