# Generated by Django 2.1.3 on 2018-11-22 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, to='shop.Cart'),
        ),
    ]
