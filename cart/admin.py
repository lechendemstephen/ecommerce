from django.contrib import admin # type: ignore
from .models import Cart, CartItem
# Register your models here.

class CartAdmin(admin.ModelAdmin): 
    list_display = ('user', 'created_date')

class CartItemAdmin(admin.ModelAdmin): 
    list_display = ('product', 'cart', 'quantity')


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)


