from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('cart', views.cart, name='cart'),
    path('cart/add/<int:id>/<int:count>', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('product/<int:id>', views.product, name='product')
]
