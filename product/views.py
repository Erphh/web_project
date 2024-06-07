from django.shortcuts import render, get_object_or_404
from .models import Product, Category, DiscountCode, Cart
from .forms import ProductForm, DiscountCodeForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'shop/product_detail.html', {'product': product})

def apply_discount(request, code):
    discount = get_object_or_404(DiscountCode, code=code)
    return render(request, 'shop/apply_discount.html', {'discount': discount})

