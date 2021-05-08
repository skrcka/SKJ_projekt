from django import forms
from .models import Product, CartItem, Order, OrderItem, DeliveryService, PaymentMethod
from django.contrib.auth import get_user_model

class LoginForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
