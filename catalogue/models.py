from django.db import models

# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=500)
    product_price = models.CharField(max_length=500)
    product_image = models.CharField(max_length=20000, null=True, blank=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    product_name = models.CharField(max_length=500)
    product_price = models.CharField(max_length=500)
    product_image = models.CharField(max_length=20000, null=True, blank=True)

    def __str__(self):
        return self.product_name
