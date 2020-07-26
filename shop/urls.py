from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('cart', views.cart),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear')
]