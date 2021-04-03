from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from Project.forms.comment_form import ProjectCommentForm
from Project.models.user_project import UserProject,ProjectComment
from Project.forms.report_form import ProjectReportForm
from datetime import datetime
from django.db.models import Avg

def show(request,project_id):
    project = get_object_or_404(UserProject, id=project_id)
    if request.method == "GET":
        print("testing")
        form = ProjectCommentForm()
        reportForm = ProjectReportForm()
        rate = project.projectRated.all().aggregate(Avg('rate'))["rate__avg"]


        return render(request,"project/show.html",{'form':form,'reportForm':reportForm, 'project':project ,
        'rate':rate, 'yellowRate': range(1, int(rate)+1), 'blackRate':range(int(rate+1),6)})


def comment(request):
    comm = ProjectComment.objects.create(
        comment_body=request.POST.get('comment_body'), user_id=request.POST.get('user_id'),
        project_id=request.POST.get('project_id'),

    )

    return HttpResponse("dona ya 7amdana")
