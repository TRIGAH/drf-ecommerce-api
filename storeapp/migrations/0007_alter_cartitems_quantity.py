# Generated by Django 5.0.3 on 2024-04-02 17:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("storeapp", "0006_alter_product_slug_alter_productimage_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cartitems",
            name="quantity",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
