from django import forms
from Project.models.user_project import UserProject
from django.contrib.admin import widgets


class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(forms.ModelForm):

    class Meta:
        model = UserProject
        fields = ("title", "details", "total_target", "start_date", "end_date", "category")
        widgets = {'start_date': DateInput(), 'end_date': DateInput()}