from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from Project.forms.comment_form import ProjectCommentForm
from Project.models.user_project import UserProject,ProjectComment, ProjectRate, ProjectReport
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
        if rate == None:
            rate=0


        return render(request,"project/show.html",{'form':form,'reportForm':reportForm, 'project':project ,
        'rate':rate, 'yellowRate': range(1, int(rate)+1), 'blackRate':range(int(rate+1),6)})


def comment(request):
    comm = ProjectComment.objects.create(
        comment_body=request.POST.get('comment_body'), user_id=request.POST.get('user_id'),
        project_id=request.POST.get('project_id'),
    )

    return redirect( "list")

def report(request):
    report = ProjectReport.objects.create(
        report_body=request.POST.get('report_body'), user_id=request.POST.get('user_id'),
        project_id=request.POST.get('project_id'),
    )
    return redirect( "list")

def rate(request):
    if request.is_ajax():
        previous_rate_count = ProjectRate.objects.filter(project_id=request.GET.get('proectId'), user_id=request.GET.get('userId')).count()
        if previous_rate_count == 0:
            rate = ProjectRate.objects.create(
                rate=float(request.GET.get('rate')), user_id=request.GET.get('userId'),
                project_id=request.GET.get('proectId'),
            )
        else:
            previous_rate_count = ProjectRate.objects.filter(project_id=request.GET.get('proectId'),
                                                             user_id=request.GET.get('userId')).update(rate=float(request.GET.get('rate')))

    return HttpResponse("dona ya 7amdana")
