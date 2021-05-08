from django.contrib import admin
from .models import Product
from .models import CartItem
from .models import DeliveryService
from .models import PaymentMethod
from .models import Order
from .models import OrderItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_id', 'count')

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'payment_method_id', 'delivery_service_id', 'street', 'city', 'country', 'psc', 'note')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'count', 'order_id')

admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartAdmin)
admin.site.register(DeliveryService, DeliveryAdmin)
admin.site.register(PaymentMethod, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
