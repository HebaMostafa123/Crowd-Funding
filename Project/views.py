from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # call landing page in dir home/index.html
    # list all Departments
    return HttpResponse("Hello world")

