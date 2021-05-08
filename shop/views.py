from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .models import Product
from .models import CartItem
from .forms import LoginForm
from .forms import OrderForm
from .forms import CartItemForm
from .forms import CartItemFormSet
from django.contrib.auth import get_user_model


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', 
                    {'products': products})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/shop')
        else:
            form = LoginForm(request.POST)
            return render(request, 'login.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def order_new(request):
    cart = CartItem.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        for item in cart:
            request.POST['']
        model_instance = form.save(commit=False)
    else:
        form = OrderForm()
        return render(request, 'order_new.html', {'form': form, 'cart': cart})

def logout_view(request):
    logout(request)
    return redirect('/shop')

def product(request, id):
    p = Product.objects.filter(id=id).first()
    return render(request, 'product.html', 
                    {'p': p})


@login_required
def cart(request):
    if request.method == 'POST':
        form = CartItemFormSet(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CartItemFormSet(queryset=CartItem.objects.filter(user_id=request.user.id))
    return render(request, 'cart.html', 
                    {'form': form})

@login_required
def orders_view(request):
    orders = Order.objects.filter(user_id=request.user.id)
    return render(request, 'orders.html', 
                    {'orders': orders})

@login_required
def cart_add(request, id, count):
    CartItem.objects.update_or_create(product_id=id, user_id=request.user.id, count=count)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def cart_remove(request, id):
    CartItem.objects.filter(id=id, user_id=request.user.id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def cart_clear(request):
    cart = CartItem.objects.filter(user_id=request.user.id).delete()
    return render(request, 'cart.html', 
                    {'cart': cart})
