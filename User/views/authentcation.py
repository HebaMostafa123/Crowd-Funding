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
#     form_class= SignUpForm
#     template_name ='registration/registration.html'
#     success_url= reverse_lazy('login')


    
