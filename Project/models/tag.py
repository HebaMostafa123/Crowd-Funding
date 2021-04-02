from django.db import models
from .user_project import UserProject
from datetime import datetime


class Tag(models.Model):
     project = models.ForeignKey(UserProject, on_delete=models.CASCADE)
     tag_name = models.CharField(max_length=200)
     created_at = models.DateTimeField(default=datetime.now, blank=True)
     updated_at = models.DateTimeField()