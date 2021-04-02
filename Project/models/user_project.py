from django.db import models
from .user import CrowdUser
from .category import Category
from datetime import datetime


class UserProject(models.Model):
    owner = models.ForeignKey(CrowdUser, on_delete=models.CASCADE, related_name="projectOwner")
    title = models.CharField(max_length=200)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_target = models.DecimalField(max_digits=9, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_cancelled = models.BooleanField(default=False)
    user_donation = models.ManyToManyField(CrowdUser, through='ProjectDonation', related_name="user_donation_join")
    user_comment = models.ManyToManyField(CrowdUser, through='ProjectComment', related_name="user_comment_join")
    user_report = models.ManyToManyField(CrowdUser, through='ProjectReport', related_name="user_report_join")
    user_rate = models.ManyToManyField(CrowdUser, through='ProjectRate', related_name="user_rate_join")
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField()


class ProjectComment(models.Model):
    user = models.ForeignKey(CrowdUser, on_delete=models.CASCADE, related_name="projectCommenter")
    project= models.ForeignKey(UserProject, on_delete=models.CASCADE ,related_name="projectCommented")
    comment_body= models.TextField()
    created_at= models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField()

class ProjectReport(models.Model):
    user = models.ForeignKey(CrowdUser, on_delete=models.CASCADE, related_name="projectReporter")
    project= models.ForeignKey(UserProject, on_delete=models.CASCADE, related_name="projectReported")
    report_body= models.TextField()
    created_at= models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField()

class ProjectRate(models.Model):
    user = models.ForeignKey(CrowdUser, on_delete=models.CASCADE , related_name="projectRater")
    project= models.ForeignKey(UserProject, on_delete=models.CASCADE, related_name="projectRated")
    rate= models.IntegerField()
    created_at= models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField()

class ProjectDonation(models.Model):
    user = models.ForeignKey(CrowdUser, on_delete=models.CASCADE, related_name="projectDonnater")
    project= models.ForeignKey(UserProject, on_delete=models.CASCADE, related_name="projectDonnated")
    amount= models.DecimalField(max_digits=9, decimal_places=2)
    created_at= models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField()