from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=100)
    profile_picutre = forms.ImageField()

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'password1', 'password2',
            'phone_number', 'email', 'profile_picutre'
        )
