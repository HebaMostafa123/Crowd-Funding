from django import forms
from Project.models.user_project import ProjectReport
from Project.models.user_project import UserProject


class ProjectReportForm(forms.ModelForm):

    class Meta:
        model = ProjectReport
        fields = ("report_body",)
