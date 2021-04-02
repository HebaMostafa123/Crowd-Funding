from django.db import models
from .user_project import UserProject
from datetime import datetime


class ProjectPicture(models.Model):
    project = models.ForeignKey(UserProject, on_delete=models.CASCADE, related_name="projectPictureProject")
    project_picture = models.ImageField(blank=True, upload_to='images/project/')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField()