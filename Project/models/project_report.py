from django.db import models
from .user_project import UserProject
from .user import User
from datetime import datetime


class ProjectReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project= models.ForeignKey(UserProject, on_delete=models.CASCADE)
    report_body= models.TextField()
    created_at= models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField()