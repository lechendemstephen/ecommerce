from django.shortcuts import render # type: ignore
from .models import Products
from django.db.models import Q # type: ignore
# Create your views here.


def store(request): 
    products = Products.objects.all()


    context = {
            "products": products,
           
        }


    return render(request, 'ecommerce/pages/store.html', context)

def product_detail(request, product_slug): 

    product = Products.objects.filter(slug=product_slug).first()



    context = {
        "product": product
    }



    return render (request, 'ecommerce/pages/single_product.html', context)