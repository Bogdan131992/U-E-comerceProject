from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.views import _cart_id

from carts.views import CartItem

# Create your views here.

def shop (request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, category_url=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context= {
        'products': products,
        'product_count' :  product_count,
    }
    return render(request, 'shop/shop.html', context)

def product_detail (request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__category_url=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists()
        


    except Exception as e:
        raise e
    
    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'shop/product_detail.html', context)
