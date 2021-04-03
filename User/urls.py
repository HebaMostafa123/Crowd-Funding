from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls import path,include
from .views import authentcation

urlpatterns = [
    path('user/register', authentcation.UserRegisterView.as_view(),name='register'),
   
   
]
