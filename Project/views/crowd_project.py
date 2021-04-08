from datetime import datetime

from django.db.models import Avg
from django.forms import modelformset_factory
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import RequestContext
from Project.forms.project_form import ImageForm, ProjectForm, TagForm
from Project.models import ProjectPicture
from Project.models.category import Category
from Project.models.featured_project import FeaturedProject
from Project.models.project_picture import ProjectPicture
from Project.models.tag import Tag
from Project.models.user_project import ProjectRate, UserProject


def index(request):
    projectPic = []
    # get highest rated project
    highest_rated_projects_ids = ProjectRate.objects.values_list('project_id', flat=True).annotate(
        avg=Avg('rate')).order_by('-avg')[:5]
    highest_rated_projects = UserProject.objects.filter(projectRated__in=list(highest_rated_projects_ids))
    # get recent projects
    recentProjects = UserProject.objects.all().order_by('-created_at')[:6]
    # get featured projects
    featuredProjects = FeaturedProject.objects.all().order_by('-created_at')[:5]
    featuredProjectsDic = projectZipFeatured(featuredProjects, projectPic)
    projectRecentDic = projectZip(recentProjects, projectPic)

    categories = Category.objects.all()

    if request.method == "POST":
        # Search by tag
        tags = Tag.objects.filter(tag_name=request.POST.get("search"))
        filteredProjects = []
        for tag in tags:
            filteredProjects.append(UserProject.objects.get(id=tag.project_id))
        projectDic = projectZip(filteredProjects, projectPic)
        return render(request, "project/index.html", {'projects': projectDic, "recentProjects": projectRecentDic,
                                                      "featuredProjectsDic": featuredProjectsDic,
                                                      "highest_rated_projects": highest_rated_projects})

    return render(request, "project/index.html",
                  {"recentProjects": projectRecentDic, "featuredProjectsDic": featuredProjectsDic,
                   "highest_rated_projects": highest_rated_projects, "categories": categories})


def projectZip(projects, projectPic):
    projectDic = {}

    for project in projects:
        print("helooo")
        projectPic.append(ProjectPicture.objects.filter(project_id=project.id)[0].project_picture.url)
    for project in projects:
        for picture in projectPic:
            projectDic[project] = picture
            projectPic.remove(picture)
            break
    return projectDic


def projectZipFeatured(projects, projectPic):
    projectDic = {}

    for project in projects:
        print("helooo")
        projectPic.append(ProjectPicture.objects.filter(project_id=project.project_id)[0].project_picture.url)
    for project in projects:
        for picture in projectPic:
            projectDic[project] = picture
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
        tagToString += tag.tag_name + " "

    # print(tagToString)
    form = ProjectForm(instance=project)
    return render(request, 'project/edit.html', {'project': project, 'form': form, 'tags': tagToString})


def update(request, project_id):
    project = UserProject.objects.get(id=project_id)
    form = ProjectForm(request.POST, instance=project)
    tagToUpdate = Tag.objects.filter(project_id=project_id).delete()
    newTags = request.POST.get("tags").split()
    for currentTag in newTags:
        tag = Tag()
        tag.tag_name = currentTag
        tag.project_id = project.id
        tag.updated_at = datetime.now()
        tag.save()

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

            # add project owner
            project.owner_id = request.user.id
            project.save()

            # add project tags
            for currentTag in tags:
                tag = Tag()
                tag.tag_name = currentTag
                tag.project_id = project.id
                tag.updated_at = datetime.now()
                tag.save()

            # add project images
            for current_image in images:
                image = current_image
                photo = ProjectPicture(project=project, project_picture=image, updated_at=datetime.now())
                photo.save()
            return redirect('list')
        else:
            print(form.errors)

            return HttpResponse(form.errors)


def delete(request, project_id):
    project = get_object_or_404(UserProject, id=project_id)
    project.delete()
    return redirect("list")


def featuredProjects(request):
    print(request.method)
    projectPic = []
    featuredProjects = FeaturedProject.objects.all().order_by('-created_at')[:6]
    # return HttpResponse(featuredProjects)
    # projectDic = projectZip(featuredProjects, projectPic)
    #
    # return render(request, "project/index.html", {"featuredProjects": projectDic})


def category_list(request, category_id):
    projects = UserProject.objects.filter(category_id=category_id)
    return render(request, "project/category.html", {'projects': projects})
