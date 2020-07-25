from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import Cart


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', 
                    {'products': products})


def cart(request):
    cart = Cart.objects.all()[0]
    return render(request, 'cart.html', 
                    {'cart': cart})