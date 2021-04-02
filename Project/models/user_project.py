from django.db import models
from .user import User
from .category import Category
# from .project_comment import ProjectComment
from datetime import datetime


class UserProject(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_target = models.DecimalField(max_digits=9, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_cancelled = models.BooleanField(default=False)
    user_donation = models.ManyToManyField(User)
    user_comment = models.ManyToManyField(User)
    user_report = models.ManyToManyField(User)
    user_rate = models.ManyToManyField(User)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField()
