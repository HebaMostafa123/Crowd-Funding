from datetime import datetime

from django.db import models

from .user_project import UserProject


class FeaturedProject(models.Model):
    project = models.ForeignKey(
        UserProject, on_delete=models.CASCADE, related_name="projectFeatureProject"
    )
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.project.title
