from __future__ import unicode_literals
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    lagersaldo = models.IntegerField()
    description = models.TextField()
    main_image = models.ImageField()


class DetailedProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField()