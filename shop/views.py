from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .models import Product
from .models import CartItem
from .models import OrderItem
from .models import Order
from .forms import LoginForm
from .forms import OrderForm
from .forms import SignUpForm
from .forms import CartItemForm
from .forms import CartItemFormSet
from .forms import UserEditForm
from .forms import PasswordChangeCustomForm
from .forms import ProductEditForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', 
                    {'products': products})

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
        if user is not None:
            login(request, user)
            return redirect('/shop')
        form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

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

@login_required
def order_new(request):
    cart = CartItem.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            oid = Order.objects.filter(user_id=request.user.id).last().id
            cartitems = CartItem.objects.filter(user_id=request.user.id)
            for item in cartitems:
                orderitem = OrderItem()
                orderitem.product = item.product
                orderitem.count = item.count
                orderitem.order = order
                orderitem.save()
            cartitems.delete()
            return redirect('/shop')
    form = OrderForm()
    return render(request, 'order_new.html', {'form': form, 'cart': cart})

def logout_view(request):
    logout(request)
    return redirect('/shop')

def product(request, id):
    p = Product.objects.filter(id=id).first()
    user = request.user
    return render(request, 'product.html', 
                    {'p': p, 'user': user})

@staff_member_required(login_url='/shop/login')
def product_edit(request, id):
    if request.method == 'POST':
        form = ProductEditForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.id = id
            item.save()
            return redirect(f'/shop/product/{id}')
    else:
        form = ProductEditForm(instance=Product.objects.filter(id=id).first())
    return render(request, 'product_edit.html', 
                    {'form': form})

@login_required
def order_detail(request, id):
    o = Order.objects.filter(id=id).first()
    ois = OrderItem.objects.filter(order_id=id)
    return render(request, 'order_detail.html', 
                    {'o': o, 'ois': ois})

@login_required
def account_detail(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('/shop/myaccount')
    else:
        form = UserEditForm(instance=request.user)
    return render(request, 'account_detail.html', 
                    {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeCustomForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('account_detail')
    else:
        form = PasswordChangeCustomForm(request.user)
    user = request.user
    return render(request, 'change_password.html', {
        'form': form, 'user': user
    })

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
