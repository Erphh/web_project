
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from loginpage.models import Account


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        level = self.get_level()
        if level is None:
            level = 0
        if level > 5:
            raise ValueError("Maximum depth of 5 exceeded")
        super().save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField()
    description = models.TextField()
    category = TreeForeignKey(Category, related_name='loginpage', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='loginpage/images/')

    def __str__(self):
        return f'Image for {self.product.name}'

class ProductVideo(models.Model):
    product = models.ForeignKey(Product, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='loginpage/videos/')

    def __str__(self):
        return f'Video for {self.product.name}'
class DiscountCode(models.Model):
    code = models.CharField(max_length=50)
    percentage = models.FloatField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    max_discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    applicable_products = models.ManyToManyField(Product, blank=True)
    applicable_categories = models.ManyToManyField(Category, blank=True)

    def __str__(self):
        return self.code

class Cart(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)