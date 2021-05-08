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

class DeliveryService(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    def __str__(self):
        return f'{self.name}({self.price})'

class PaymentMethod(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.name}'

class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=0)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, default=0)
    delivery_service = models.ForeignKey(DeliveryService, on_delete=models.CASCADE, default=0)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    psc = models.CharField(max_length=5)
    note = models.CharField(max_length=255)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=0)
    count = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=0)
