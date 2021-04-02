from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls import path,include
from . import views

urlpatterns = [
    # path('', include('Project.urls')),
    path('home',views.index)
]
