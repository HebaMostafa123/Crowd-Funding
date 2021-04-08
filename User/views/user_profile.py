from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from User.models import User


def show(request):
    current_user=get_object_or_404(User,id=request.user.id)
    userPic=User.objects.filter(id=request.user.id)[0].profile_picutre.url
    return render(request,"user/show.html",{'user':current_user,'pic':userPic})



