from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    image_url = models.CharField(max_length=2083)


class Cart(models.Model):
    products_list=models.ManyToManyField(Product,blank=True)
    total=models.IntegerField(default=0)

    def count_cart_items(self):
         return int(self.cart_items)