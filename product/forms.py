# product/forms.py
from django import forms
from .models import Product, ProductImage, ProductVideo, DiscountCode

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price']

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['product', 'image']

class ProductVideoForm(forms.ModelForm):
    class Meta:
        model = ProductVideo
        fields = ['product', 'video']

class DiscountCodeForm(forms.ModelForm):
    class Meta:
        model = DiscountCode
        fields = ['code', 'percentage', 'amount', 'max_discount', 'applicable_products', 'applicable_categories']
