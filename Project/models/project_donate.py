from django.db import models
from .user_project import UserProject
from .user import User
from datetime import datetime


class ProjectDonation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project= models.ForeignKey(UserProject, on_delete=models.CASCADE)
    amount= models.DecimalField(max_digits=9, decimal_places=2)
    created_at= models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField()