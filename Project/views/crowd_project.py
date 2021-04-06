from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from Project.forms.project_form import ProjectForm 
from Project.forms.project_form import TagForm
from Project.models.user_project import UserProject
from Project.models.tag import Tag
from datetime import datetime

def index(request):
    return HttpResponse("Hello world")


def project_list(request):
   # print(UserProject.objects.all())
    return render(request, "project/project_list.html",{'projects':UserProject.objects.all()})


def edit(request, project_id):
    project = UserProject.objects.get(id=project_id)
    tags=Tag.objects.filter(project_id=project_id)

    tagToString=""
    for tag in tags:
        tagToString+=tag.tag_name+" "
        
    #print(tagToString)
    form = ProjectForm(instance=project)
    return render(request, 'project/edit.html', {'project': project, 'form': form,'tags':tagToString})


def update(request, project_id):
    project = UserProject.objects.get(id=project_id)
    form = ProjectForm(request.POST, instance=project)
    tagToUpdate=Tag.objects.filter(project_id=project_id).delete()
    newTags=request.POST.get("tags").split()
    for currentTag in newTags:
                tag=Tag()
                tag.tag_name=currentTag
                tag.project_id=project.id
                tag.updated_at=datetime.now()
                tag.save()

    print("haha new tag: ")
    print(tagToUpdate)
    
    # for tag
    if form.is_valid():
        form.save()
        return redirect("list")
    return render(request, 'project/edit.html', {'project': project})


def project_form(request):
    if request.method == "GET":
        print("testing")
        form=ProjectForm()
        

        return render(request,"project/project_form.html",{'form':form})
    else:
        tags=request.POST.get("tags").split()      
        #print(request.POST.get("tags"))
        form=ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)
            #add project owner
            project.owner_id=1
            project.save()
            for currentTag in tags:
                tag=Tag()
                tag.tag_name=currentTag
                tag.project_id=project.id
                tag.updated_at=datetime.now()
                tag.save()
        return redirect('list')

def delete(request, project_id):
    project = get_object_or_404(UserProject, id=project_id)
    project.delete()
    return redirect( "list")

