# product/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth import get_user_model
User = get_user_model()


app_name="home_page"

urlpatterns = [
    path("",views.home_page,name="home_page"),  
]
