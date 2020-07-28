from django.contrib import admin
from .models import Product
from .models import CartItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class CartAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_id', 'count')


admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartAdmin)
