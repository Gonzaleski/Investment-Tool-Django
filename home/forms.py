from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):

    username    = forms.CharField(max_length=150)
    first_name  = forms.CharField(max_length=150)
    last_name   = forms.CharField(max_length=150)
    email       = forms.EmailField(max_length=150)
    password1   = forms.CharField(widget=forms.PasswordInput())
    password2   = forms.CharField(widget=forms.PasswordInput(), help_text="Enter your password again")
    class Meta:
        model= User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']