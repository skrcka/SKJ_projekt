from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .models import CartItem


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', 
                    {'products': products})


@login_required(login_url="/users/login")
def cart(request):
    cart = CartItem.objects.filter(user_id=request.user.id)
    return render(request, 'cart.html', 
                    {'cart': cart})


@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = CartItem.objects.filter(user_id=request.user.id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = CartItem.objects.filter(user_id=request.user.id)
    return render(request, 'cart.html', 
                    {'cart': cart})


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = CartItem.objects.filter(user_id=request.user.id)
    return render(request, 'cart.html', 
                    {'cart': cart})