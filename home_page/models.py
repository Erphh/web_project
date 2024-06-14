from django.db import models
from mptt.models import MPTTModel, TreeForeignKey





class HomeBanner(models.Model):
    image = models.ImageField(upload_to='home_banners/')
    link = models.URLField()

    def __str__(self):
        return f'Banner {self.id}'
class BigProduct(models.Model):
    image = models.ImageField(upload_to='big_product/')
    link = models.URLField()

    def __str__(self):
        return f'Banner {self.id}'

