from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from .views import authentcation, user_profile

urlpatterns = [
    path("register/", authentcation.UserRegisterView, name="register"),
    path("login/", authentcation.loginPage, name="login"),
    path(
        "activate/<uidb64>/<token>",
        authentcation.ActivateAccountView.as_view(),
        name="activate",
    ),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
    path("project/user", user_profile.show),
    # path("edit_profile/", authentcation.UserEditView.as_view(), name="edit_profile"),
    url(r"^user/(?P<user_id>\d+)/$", authentcation.edit, name="edit_profile"),
    url(
        r"^user/(?P<user_id>\d+)/update$",
        authentcation.update,
        name="user_update",
    ),
    url(r"^user/(?P<user_id>\d+)/delete$", authentcation.delete, name="user_delete"),
]
