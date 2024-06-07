# shop/admin.py
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Category, Product, DiscountCode, Cart, CartItem, ProductImage, ProductVideo

admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Product)
admin.site.register(DiscountCode)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(ProductImage)
admin.site.register(ProductVideo)
