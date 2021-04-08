from django import forms
from django.contrib.admin import widgets
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django_countries import countries

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
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "phone_number",
            "email",
            "profile_picutre",
        )


class DateInput(forms.DateInput):
    input_type = "date"


class UserEditForm(UserChangeForm):
    # email = forms.EmailField()
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # phone_number = forms.CharField(max_length=100)
    profile_picutre = forms.ImageField()
    # faceboock_url = User.faceboock_url
    # country = User.country
    # # birth_date = forms.DateField()

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "profile_picutre",
            "faceboock_url",
            "country",
            "birth_date",
        )
        widgets = {"birth_date": DateInput()}
