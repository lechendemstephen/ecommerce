from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from store.models import Products
from .models import Cart, CartItem
# Create your views here.

def cart_view(request):
    cartitems = CartItem.objects.all()
    # getting the total price for a particular productin Cart
   

    
    context = {
        "cartitems": cartitems,
       # "grand_total": grand_total

     
    }


    return render(request, 'ecommerce/pages/cart.html', context)

def add_to_cart(request, product_id): 
    product = get_object_or_404(Products, pk=product_id)
    
    cart, created = Cart.objects.get_or_create(user=request.user)

    cartitem, created = CartItem.objects.get_or_create(product=product, cart=cart)

   
    if not created: 
        cartitem.quantity +=1 
    cartitem.save()
    
  
   
    return redirect('cart')

def delete_cartitem(request, product_id): 
   
    cartitem = CartItem.objects.filter(product__id = product_id)
    cartitem.delete()
    
    return redirect('cart')


    


