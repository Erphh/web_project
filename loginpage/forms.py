from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

from django import forms

from loginpage.models import Account



class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=60, required=True)
    name = forms.CharField(max_length=30, required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model =  Account
        fields = ['name', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        del self.fields['password2']

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    emaill = forms.EmailField(max_length=60, required=True)
    class Meta:
        model = Account
        fields = ('emaill', 'password')

    def clean(self):
        if self.is_valid():
            emaill = self.cleaned_data['emaill']
            password = self.cleaned_data['password']

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, required=True, label="Enter OTP")
