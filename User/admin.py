from django.contrib import admin

# Register your models here.
from django.contrib import admin

from Project.models.category import Category
from Project.models.user_project import ProjectReport, CommentReport
from User.models import User

# Register your models here.
admin.site.register(User) 
admin.site.register(Category)
admin.site.register(ProjectReport)
admin.site.register(CommentReport)
