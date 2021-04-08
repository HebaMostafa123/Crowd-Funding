from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from Project.forms.comment_form import ProjectCommentForm
from Project.models.user_project import UserProject,ProjectComment, ProjectRate, ProjectReport,CommentReport,ProjectDonation
from Project.forms.report_form import ProjectReportForm
from Project.models.project_picture import ProjectPicture
from datetime import datetime
from django.db.models import Avg
from User.models import User

def show(request,project_id):
    if not request.user.is_authenticated:
        return redirect('login')

    project = get_object_or_404(UserProject, id=project_id)
    projectPics=ProjectPicture.objects.filter(project_id=project.id)
    picArr=[]
    for pic in projectPics:       
        picArr.append(pic.project_picture.url)
    
    if request.method == "GET":
        print("testing")
        form = ProjectCommentForm()
        reportForm = ProjectReportForm()
        rate = project.projectRated.all().aggregate(Avg('rate'))["rate__avg"]
        if rate == None:
            rate=0


        return render(request,"project/show.html",{'form':form,'reportForm':reportForm, 'project':project ,
        'rate':rate, 'yellowRate': range(1, int(rate)+1), 'blackRate':range(int(rate+1),6),"pictures":picArr})


def comment(request):
    if not request.user.is_authenticated:
        return redirect('login')

    comm = ProjectComment.objects.create(
        comment_body=request.POST.get('comment_body'), user_id=request.POST.get('user_id'),
        project_id=request.POST.get('project_id'),
    )

    return redirect( "list")

def report(request):
    if not request.user.is_authenticated:
        return redirect('login')
    report = ProjectReport.objects.create(
        report_body=request.POST.get('report_body'), user_id=request.POST.get('user_id'),
        project_id=request.POST.get('project_id'),
    )
    return redirect( "list")

def reportComment(request):
    if not request.user.is_authenticated:
        return redirect('login')

    report = CommentReport.objects.create(
        report_body=request.POST.get('report_body'), user_id=request.POST.get('user_id'),
        commment_id=request.POST.get('commment_id'),
    )
    return redirect("list")

def rate(request):
    if not request.user.is_authenticated:
        return redirect('login')

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


def donate(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.is_ajax():
            userBalance = User.objects.values_list('balance', flat=True).filter(id=request.GET.get('userId'))
            print("hhhh")
            balance = userBalance[0]
            if( int(userBalance[0]) >= int(request.GET.get("donate"))):
                dona = ProjectDonation.objects.create(
                    amount=float(request.GET.get('donate')), user_id=request.GET.get('userId'),
                    project_id=request.GET.get('proectId'))
                User.objects.filter(id=request.GET.get('userId')).update(balance=int(userBalance[0]) - int(request.GET.get("donate")))
                return HttpResponse("donated successfully")

    return HttpResponse("you don't have this amount of money in your balance")
