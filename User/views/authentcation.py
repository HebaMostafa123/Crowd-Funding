from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import logout
from User.forms import SignUpForm


def logoutUser(request):
        logout(request)
        return redirect('login')
        
class UserRegisterView(generic.CreateView):
    form_class= SignUpForm
    template_name ='registration/registration.html'
    success_url= reverse_lazy('login')

    
