# Generated by Django 5.0.3 on 2024-05-15 07:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_product_availability_product_spec"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="discounted_price",
        ),
    ]
