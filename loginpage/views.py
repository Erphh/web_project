from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CreateUserForm, LoginForm,OTPForm
from .models import Account
import random
from django.core.mail import send_mail
from django.conf import settings

def login_page(request):
    reg_form = CreateUserForm()
    login_form = LoginForm()
   
    if request.method == "POST":
        if 'register' in request.POST:
            reg_form = CreateUserForm(request.POST)
            if reg_form.is_valid():
                user = reg_form.save()
                send_otp_email(user)
                messages.success(request, 'Registration successful. Please verify your OTP.')
                return redirect('loginpage:otp_verification', user_id=user.id)
        elif 'login' in request.POST:
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                email = login_form.cleaned_data.get('emaill')
                raw_password = login_form.cleaned_data.get('password')
                account = authenticate(email=email, password=raw_password)
                if account:
                    if account.is_authenticate:
                        login(request, account)
                        return redirect('home_page:home_page')
                    else:
                        send_otp_email(user)
                        messages.error(request, 'Please verify your OTP first.')
                        return redirect('loginpage:otp_verification', user_id=account.id)
                else:
                    messages.error(request, 'Invalid credentials')

    context = {
        "form2": reg_form,
        "form1": login_form,
    
    }

    return render(request, "loginpage/login.html", context)

def otp_verification(request, user_id):
    otp_form = OTPForm()
    user = get_object_or_404(Account, id=user_id)
    
    if request.method == "POST":
        otp_form = OTPForm(request.POST)
        if otp_form.is_valid():
            otp = otp_form.cleaned_data.get('otp')
            if user.verify_otp(otp):
                user.is_active = True
                user.save()
                messages.success(request, 'OTP verified successfully. You can now log in.')
                return redirect('loginpage:loginpage')
            else:
                messages.error(request, 'Invalid OTP. Please try again.')
    
    context = {
        'user': user,
        'form3': otp_form,
    }

    return render(request, "loginpage/otp.html", context)

def send_otp_email(user):
    otp = random.randint(10000, 99999)
    user.otp_secret = otp
    user.save()
    subject = 'Your OTP Code'
    message = f'Your OTP code is: {user.otp_secret}'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)


