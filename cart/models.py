from django.db import models # type: ignore
from store.models import Products
from accounts.models import User
# Create your models here.

class Cart(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.user.username
    


class CartItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 

        return self.product.name
    

    def total_unit_price(self): 
        total_unit_price = self.quantity * self.product.price

        return total_unit_price
    
    def grand_total(self): 
        grand = 0 
        total = self.quantity * self.product.price
        grand += total
        
        return grand
    
 
    