# Generated by Django 3.2.12 on 2022-03-09 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_shoppingcart_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Image',
            new_name='image',
        ),
    ]
