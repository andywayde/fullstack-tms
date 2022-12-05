from django import forms
from .models import Project

from django.forms.widgets import DateInput

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'
        labels = {
            'is_completed': 'Completed',
            'total': 'Total (RUB)',
        }
        widgets = {
            'deadline': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['client'].empty_label = "Select Client"