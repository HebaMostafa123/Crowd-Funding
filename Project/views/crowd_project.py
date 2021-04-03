from django.shortcuts import render,redirect
from django.http import HttpResponse
from Project.forms.project_form import ProjectForm
from Project.models.user_project import UserProject
def index(request):
     return HttpResponse("Hello world")
def project_list(request):
    print(UserProject.objects.all())
    return render(request,"project/project_list.html",{'projects':UserProject.objects.all()})
def project_form(request):
    if request.method == "GET":
        print("testing")
        form=ProjectForm()
        return render(request,"project/project_form.html",{'form':form})
    else:       
        print(request.POST)
        form=ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            print("haha saved")
        return redirect('/project/list')
        
def project_delete(request):
    return

