# Generated by Django 5.1.3 on 2024-11-24 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_stock_quantity_product_stock_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sku',
        ),
    ]