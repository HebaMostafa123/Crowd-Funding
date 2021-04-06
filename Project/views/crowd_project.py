from django.forms import modelformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext

from Project.forms.project_form import ProjectForm, ImageForm
from Project.forms.project_form import TagForm
from Project.models.user_project import UserProject
from Project.models.tag import Tag
from datetime import datetime

from Project.models import ProjectPicture


def index(request):
    return HttpResponse("Hello world")


def project_list(request):
    print(UserProject.objects.all())
    return render(request, "project/project_list.html",{'projects':UserProject.objects.all()})


def edit(request, project_id):
    project = UserProject.objects.get(id=project_id)
    form = ProjectForm(instance=project)
    return render(request, 'project/edit.html', {'project': project, 'form': form})


def update(request, project_id):
    project = UserProject.objects.get(id=project_id)
    form = ProjectForm(request.POST, instance=project)
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
        tags=request.POST.get("tags").split()
        form=ProjectForm(request.POST)
        if form.is_valid():
            project=form.save(commit=False)

            #add project owner
            project.owner_id=1
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
            print(form.errors)


def delete(request, project_id):
    project = get_object_or_404(UserProject, id=project_id)
    project.delete()
    return redirect("list")
