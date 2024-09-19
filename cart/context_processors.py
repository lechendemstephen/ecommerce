from .models import CartItem 

def total_cartitem(request): 
    total_cartitems = CartItem.objects.all()
    cartitem_count = total_cartitems.count()

    return {
        "cartitem_count": cartitem_count
    }

def grand_total(request): 
    grand_total = CartItem.grand_total

    return {
        "grand_total": grand_total
    }
