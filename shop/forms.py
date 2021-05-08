from django import forms
from .models import Product, CartItem, Order, OrderItem, DeliveryService, PaymentMethod
from django.contrib.auth import get_user_model
from django.forms import modelformset_factory

class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method', 'delivery_service', 'street', 'city', 'country', 'psc', 'note']

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'count']

CartItemFormSet = modelformset_factory(CartItem, form=CartItemForm, extra=0)
