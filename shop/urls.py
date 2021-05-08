from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('cart', views.cart, name='cart'),
    path('cart/add/<int:id>/<int:count>', views.cart_add, name='cart_add'),
    path('cart/cart_remove/<int:id>', views.cart_remove, name='cart_remove'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('order/order_new/', views.order_new, name='order_new'),
    path('orders', views.orders_view, name='orders'),
    path('product/<int:id>', views.product, name='product')
]
