from django.contrib import admin
from .models import Category, Product, ProductImage, ProductVideo,DiscountCode,Cart
# Register your models here.


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductVideoInline(admin.TabularInline):
    model = ProductVideo
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductVideoInline]

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductVideo)
admin.site.register(DiscountCode)
admin.site.register(Cart)