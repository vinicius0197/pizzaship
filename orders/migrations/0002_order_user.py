# Generated by Django 2.0.3 on 2018-08-11 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.CharField(default='user', max_length=64),
        ),
    ]
