from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls import path,include
from .views import crowd_project
from .views import showProject

urlpatterns = [
    # path('', include('Project.urls')),
    path('home',crowd_project.index),
    path('project/list',crowd_project.project_list),
    path('project/form',crowd_project.project_form),
    url(r'^project/(?P<project_id>\d+)/$', showProject.show, name='item_read'),
    path('project/comment', showProject.comment, name='comment'),

]
