from django import forms
from .models import Product, CartItem, Order, OrderItem, DeliveryService, PaymentMethod
from django.contrib.auth import get_user_model
from django.forms import modelformset_factory
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class PasswordChangeCustomForm(PasswordChangeForm):
        error_css_class = 'has-error'
        old_password = forms.CharField(required=True, label='Old password: ',
                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        new_password1 = forms.CharField(required=True, label='New password: ',
                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        new_password2 = forms.CharField(required=True, label='Confirm password',
                      widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email']
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name']
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method', 'delivery_service', 'street', 'city', 'country', 'psc', 'note']
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
    def __init__(self, *args, **kwargs):
        super(ProductEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'count']

CartItemFormSet = modelformset_factory(CartItem, form=CartItemForm, extra=0)
