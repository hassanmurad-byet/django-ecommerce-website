# Generated by Django 5.0.4 on 2024-04-25 16:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cart",
            old_name="Product",
            new_name="product",
        ),
        migrations.RenameField(
            model_name="orderplaced",
            old_name="Customer",
            new_name="customer",
        ),
        migrations.RenameField(
            model_name="orderplaced",
            old_name="Product",
            new_name="product",
        ),
        migrations.RenameField(
            model_name="product",
            old_name="Product_image",
            new_name="product_image",
        ),
    ]