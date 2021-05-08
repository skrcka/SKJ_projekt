from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login', views.login_view, name='login'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('logout', views.logout_view, name='logout'),
    path('cart', views.cart, name='cart'),
    path('cart/add/<int:id>/<int:count>', views.cart_add, name='cart_add'),
    path('cart_remove/<int:id>', views.cart_remove, name='cart_remove'),
    path('cart_clear', views.cart_clear, name='cart_clear'),
    path('order_new', views.order_new, name='order_new'),
    path('order_detail/<int:id>', views.order_detail, name='order_detail'),
    path('orders', views.orders_view, name='orders'),
    path('product/<int:id>', views.product, name='product')
]
