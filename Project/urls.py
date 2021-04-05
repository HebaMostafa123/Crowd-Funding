from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from django.urls import path,include
from .views import crowd_project
from .views import showProject

urlpatterns = [
    # path('', include('Project.urls')),
    path('home',crowd_project.index),
    path('project/list',crowd_project.project_list,name="list"),
    path('project/form',crowd_project.project_form,name="form"),
    url(r'^project/(?P<project_id>\d+)/$', showProject.show, name='item_read'),
    path('project/comment', showProject.comment, name='comment'),
    url('project/rate', showProject.rate, name='rate'),
    url(r'^project/(?P<project_id>\d+)/edit$', crowd_project.edit, name='project_edit'),
    url(r'^project/(?P<project_id>\d+)/update$', crowd_project.update, name='project_update'),
    url(r'^project/(?P<project_id>\d+)/delete$', crowd_project.delete, name='project_delete'),
]
