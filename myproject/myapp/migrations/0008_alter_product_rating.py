# Generated by Django 5.0.7 on 2024-08-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
