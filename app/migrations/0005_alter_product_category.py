# Generated by Django 5.0.4 on 2024-05-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_orderplaced_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("M", "Mobile"),
                    ("L", "Laptop"),
                    ("AP", "AirPods"),
                    ("AC", "Accessories"),
                ],
                max_length=2,
            ),
        ),
    ]
