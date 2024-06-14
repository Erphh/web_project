from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product, Cart

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    images = product.images.all()   
    context = {
        'product': product,
        'images': images,
    }
    return render(request, 'product.html', context)

@login_required(login_url='loginpage:login')  
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user, defaults={'user': user})

    cart.products.add(product)
    messages.success(request, f'Product {product.name} added to your cart!')

    return redirect('product_detail', product_id=product_id)
