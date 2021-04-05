from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from User.models import User

from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    # profile_picture = forms.ImageField(blank=True,upload_to = 'images/user/')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'phone', 'email']
