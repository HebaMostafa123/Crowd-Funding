from django import forms
from Project.models.user_project import ProjectComment
from Project.models.user_project import UserProject


class ProjectCommentForm(forms.ModelForm):

    class Meta:
        model = ProjectComment
        fields = ("comment_body",)
