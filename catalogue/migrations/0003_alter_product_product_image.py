# Generated by Django 4.0.1 on 2022-01-26 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.CharField(blank=True, max_length=20000, null=True),
        ),
    ]
