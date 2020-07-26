from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class CartItem(models.Model):
    user_id=models.IntegerField(default=-1)
    product=models.ManyToManyField(Product,blank=True)
    count=models.IntegerField(default=1)