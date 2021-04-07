from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext

from Project.forms.project_form import ProjectForm, ImageForm
from Project.forms.project_form import TagForm
from Project.models.user_project import UserProject
from Project.models.project_picture import ProjectPicture
from Project.models.tag import Tag
from datetime import datetime

from Project.models import ProjectPicture


def index(request):
    print(request.method)
    projectPic=[]
       
    projectDic={}
    #Search by tag
    if request.method=="POST":
        tags=Tag.objects.filter(tag_name=request.POST.get("search"))
        filteredProjects=[]
        for tag in tags:
            filteredProjects.append(UserProject.objects.get(id=tag.project_id))
        
        projectDic=projectZip(filteredProjects,projectPic)     
        return render(request,"project/index.html",{'projects':projectDic,"recentProjects":projectDic})
    #filter by the most recent 6 projects
    recentProjects=UserProject.objects.all().order_by('-created_at')[:6]
    #return HttpResponse(recentProjects)
    projectDic=projectZip(recentProjects,projectPic)
      
    return render(request, "project/index.html",{"recentProjects":projectDic})

def projectZip(projects,projectPic):
    projectDic={}
    

    for project in projects:
             print("helooo")
             projectPic.append(ProjectPicture.objects.filter(project_id=project.id)[0].project_picture.url)
    for project in projects:
        for picture in projectPic:
            projectDic[project]=picture
            projectPic.remove(picture)
            break 
    return projectDic 
    
    

def project_list(request):
    return render(request, "project/project_list.html", {'projects': UserProject.objects.all()})


def edit(request, project_id):
    project = UserProject.objects.get(id=project_id)
    tags = Tag.objects.filter(project_id=project_id)

    tagToString = ""
    for tag in tags:
        tagToString += tag.tag_name+" "
        
    #print(tagToString)
    form = ProjectForm(instance=project)
    return render(request, 'project/edit.html', {'project': project, 'form': form,'tags':tagToString})


def update(request, project_id):
    project = UserProject.objects.get(id=project_id)
    form = ProjectForm(request.POST, instance=project)
    tagToUpdate = Tag.objects.filter(project_id=project_id).delete()
    newTags = request.POST.get("tags").split()
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
        form = ProjectForm()
        return render(request, "project/project_form.html", {'form': form})
    else:
        images = request.FILES.getlist("images")
        tags = request.POST.get("tags").split()
        form = ProjectForm(request.POST)


        if form.is_valid():
            project = form.save(commit=False)

            #add project owner
            project.owner_id = request.user.id
            project.save()

            # add project tags
            for currentTag in tags:
                tag=Tag()
                tag.tag_name = currentTag
                tag.project_id = project.id
                tag.updated_at=datetime.now()
                tag.save()

            # add project images
            for current_image in images:
                image = current_image
                photo = ProjectPicture(project=project, project_picture=image, updated_at=datetime.now())
                photo.save()
            return redirect('list')
        else:
            print("111111111111111111111111111111111111111111")
            print(form.errors)

            return HttpResponse(form.errors)


def delete(request, project_id):
    project = get_object_or_404(UserProject, id=project_id)
    project.delete()
    return redirect( "list")

