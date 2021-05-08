from django import forms
from .models import Product, CartItem, Order, OrderItem, DeliveryService, PaymentMethod
from django.contrib.auth import get_user_model
from django.forms import modelformset_factory

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method', 'delivery_service', 'street', 'city', 'country', 'psc', 'note']
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'count']

CartItemFormSet = modelformset_factory(CartItem, form=CartItemForm, extra=0)
