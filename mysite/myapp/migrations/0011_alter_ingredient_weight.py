# Generated by Django 5.0.1 on 2024-01-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_added_amount_product_using_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='weight',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
