from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from Project.forms.comment_form import ProjectCommentForm
from Project.models.user_project import UserProject,ProjectComment, ProjectRate, ProjectReport,CommentReport,ProjectDonation
from Project.forms.report_form import ProjectReportForm
from datetime import datetime
from django.db.models import Avg
from User.models import User


def donations(request):
    user_donations = ProjectDonation.objects.filter(user_id=request.user.id)
    return render(request, "project/user_donation.html", {'user_donations': user_donations})

