# views.py
from django.shortcuts import render
from django.conf import settings
import os

def home_page(request):
    banners_dir = os.path.join(settings.MEDIA_ROOT, 'home_banners')
    big_dir=os.path.join(settings.MEDIA_ROOT, 'big_product')
    banners = os.listdir(banners_dir)
    banners_urls = [os.path.join(settings.MEDIA_URL, 'home_banners', banner) for banner in banners]
    bigs = os.listdir(big_dir)
    bigs_urls = [os.path.join(settings.MEDIA_URL, 'big_product', big) for big in bigs]
    return render(request, 'home.html', {'banners': banners_urls , 'bigs':bigs_urls})
