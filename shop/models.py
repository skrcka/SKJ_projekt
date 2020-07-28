from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class CartItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=0)
    count = models.IntegerField(default=0)