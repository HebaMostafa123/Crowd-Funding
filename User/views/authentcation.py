import threading

from django.conf import settings
from django.contrib import messages

# from users.form import Usermodelform
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import DjangoUnicodeDecodeError, force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import generic
from django.views.generic import View
from six import text_type
from User.forms import SignUpForm, UserEditForm

# Create your views here.
from User.models import User
from User.utils import account_activation_token, generate_token


class EmailThread(threading.Thread):
    def __init__(self, email_message):
        self.email_message = email_message
        threading.Thread.__init__(self)

    def run(self):
        self.email_message.send()


def UserRegisterView(request):

    form = SignUpForm()
    if request.method == "POST":

        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            email = request.POST["email"]
            # email activation
            current_site = get_current_site(request)
            email_body = {
                "user": user,
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "token": account_activation_token.make_token(user),
            }

            link = reverse(
                "activate",
                kwargs={"uidb64": email_body["uid"], "token": email_body["token"]},
            )

            email_subject = "Activate your account"

            activate_url = "http://" + current_site.domain + link

            email = EmailMessage(
                email_subject,
                "Hi "
                + user.username
                + ", Please the link below to activate your account \n"
                + activate_url,
                "mai.maher003@gmail.com",
                [email],
            )
            email.send(fail_silently=False)
            EmailThread(email).start()

            messages.success(request, "Account was created for " + username)

            return redirect("login")

    context = {"form": form}
    return render(request, "registration/registration.html", context)


def edit(request, user_id):
    user = User.objects.get(id=user_id)
    form = UserEditForm(instance=user)
    return render(
        request, "registration/edit_profile.html", {"user": user, "form": form}
    )


def update(request, user_id):
    user = User.objects.get(id=user_id)
    form = UserEditForm(request.POST, instance=user)

    if form.is_valid():
        form.save()
        return redirect("list")
    return render(request, "registration/edit_profile.html", {"user": user})


def delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect("logout")


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect("login" + "?message=" + "User already activated")

            if user.is_active:
                return redirect("login")
            user.is_active = True
            user.save()

            messages.success(request, "Account activated successfully")
            return redirect("login")

        except Exception as ex:
            pass

        return redirect("login")

    # def get(self, request, uidb64, token):
    #     try:
    #         uid = force_text(urlsafe_base64_decode(uidb64))
    #         user = User.objects.get(pk=uid)
    #     except Exception as identifier:
    #         user = None
    #     if user is not None and generate_token.check_token(user, token):
    #         user.is_active = True
    #         user.save()
    #         messages.add_message(request, messages.SUCCESS,'account activated successfully')
    #         return redirect('login')

    #     return render(request, 'registration/activate_failed.html', status=401)


def loginPage(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("list")
        else:
            messages.info(request, "Email OR password is incorrect")

    context = {}
    return render(request, "registration/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")
