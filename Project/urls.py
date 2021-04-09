from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from User.views import authentcation

from .views import crowd_project, showProject, userDonation

urlpatterns = [
    # path('', include('Project.urls')),
    path("project/", crowd_project.index, name="index"),
    path("project/form", crowd_project.project_form),
    path("project/list", crowd_project.project_list, name="list"),
    path("project/form", crowd_project.project_form, name="form"),
    url(r"^project/(?P<project_id>\d+)/$", showProject.show, name="hatoom"),
    path("project/comment", showProject.comment, name="comment"),
    url("project/rate", showProject.rate, name="rate"),
    url("project/donate", showProject.donate, name="donate"),
    url("project/report", showProject.report, name="report-project"),
    path("project/userProjects", crowd_project.user_project_list, name="list"),
    url("comment/report", showProject.reportComment, name="report-comment"),
    url(
        r"^project/category/(?P<category_id>\d+)/$",
        crowd_project.category_list,
        name="category",
    ),
    url(r"^project/(?P<project_id>\d+)/edit$", crowd_project.edit, name="project_edit"),
    url(
        r"^project/(?P<project_id>\d+)/update$",
        crowd_project.update,
        name="project_update",
    ),
    url(
        r"^project/(?P<project_id>\d+)/delete$",
        crowd_project.delete,
        name="project_delete",
    ),
    path("logout", authentcation.logoutUser, name="logout"),
    path("userDonation", userDonation.donations, name="userDonation"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
