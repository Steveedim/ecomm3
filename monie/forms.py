from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Username","class": "form-control"}))

    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Enter Email","class": "form-control"}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter Password","class": "form-control"}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Repeat Password","class": "form-control"}))


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]

    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter Username", "class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Enter Password", "class": "form-control"}))

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "price", "description", "is_sold", "stock", "image"]

