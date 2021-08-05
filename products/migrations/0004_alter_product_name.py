# Generated by Django 3.2.5 on 2021-08-01 12:49

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=150, validators=[products.models.validate_name]),
        ),
    ]