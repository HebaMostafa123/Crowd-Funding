from django import forms
from .models.user_project import UserProject

class ProjectForm(forms.ModelForm):

    class Meta:
        model=UserProject
        fields=("title","details","total_target","start_date","end_date","category")