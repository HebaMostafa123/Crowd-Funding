from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from User.views import authentcation

from .views import crowd_project

urlpatterns = [
    path('home', crowd_project.index),
    path('project/list', crowd_project.project_list, name='projectlist'),
    path('project/form', crowd_project.project_form),
    path('login', authentcation.logoutUser, name='logout'),
]
