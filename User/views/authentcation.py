from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from User.forms import SignUpForm
# Create your views here.
from User.models import User

# def UserRegisterView(request):
#     if request.user.is_authenticated:
#         return redirect('/home')
#     else:
#         form = SignUpForm(request.POST)
#         if request.method == 'POST':
#             form = SignUpForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for ' + user)

#                 return redirect('login')

#         context = {'form': form}
#         return render(request, 'registration/registration.html', context)

# def loginPage(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#             user = authenticate(request, username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.info(request, 'Username OR password is incorrect')

#         context = {}
#         return render(request, '/login.html', context)

# def logoutUser(request):
#     logout(request)
#     return redirect('login')


def logoutUser(request):
    logout(request)
    return redirect('login')


def UserRegisterView(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'registration/registration.html', {'form': form})
    form_class = SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
