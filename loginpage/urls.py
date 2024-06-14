from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import CreateUserForm
from django.contrib.auth import get_user_model
User = get_user_model()


app_name="loginpage"

urlpatterns = [
    path("",views.login_page,name="login"),
    path('', auth_views.LoginView.as_view(template_name='loginpage/login.html', authentication_form=CreateUserForm)),
    path('otp-verification/<int:user_id>/', views.otp_verification, name='otp_verification'),
]
