# Generated by Django 5.0.1 on 2024-01-26 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_ingredients_options_alter_order_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredients',
            name='product',
        ),
    ]
