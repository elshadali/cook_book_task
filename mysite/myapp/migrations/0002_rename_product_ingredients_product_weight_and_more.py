# Generated by Django 5.0.1 on 2024-01-26 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredients',
            old_name='product',
            new_name='product_weight',
        ),
        migrations.RemoveField(
            model_name='ingredients',
            name='weight',
        ),
    ]
