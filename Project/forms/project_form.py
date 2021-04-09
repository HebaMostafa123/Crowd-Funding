from django import forms
from Project.models.user_project import UserProject
from Project.models.tag import Tag
from django.contrib.admin import widgets

from Project.models import ProjectPicture


class DateInput(forms.DateInput):
    input_type = 'date'


class ProjectForm(forms.ModelForm):

    class Meta:
        model = UserProject
        fields = ("title", "details", "total_target", "start_date", "end_date", "category")
        widgets = {'start_date': DateInput(), 'end_date': DateInput()}


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ("tag_name",)


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = ProjectPicture
        fields = ('image',)