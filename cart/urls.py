from django.urls import path # type: ignore
from . import views

urlpatterns = [

    path('', views.cart_view, name='cart'),
    path('cart/<int:product_id>/', views.add_to_cart, name='add_cart'),
    path('cart/delete/<int:product_id>/', views.delete_cartitem, name='delete_cart'),
    
    
]
