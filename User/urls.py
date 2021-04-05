from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from .views import authentcation

urlpatterns = [
    path('register/', authentcation.UserRegisterView, name='register'),
    path('login/', authentcation.loginPage, name="login"),
]
