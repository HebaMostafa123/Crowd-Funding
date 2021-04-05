from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls import path,include
from .views import authentcation

urlpatterns = [
    path('register/', authentcation.UserRegisterView,name='register'),
    path('login/', authentcation.loginPage,name='login'),
#    path('',registerpage, name='checkdata')
   
]
