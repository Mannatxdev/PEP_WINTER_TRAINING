from django import forms 
from .models import Task, SubTask

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']


class SubTaskForm(forms.ModelForm):
    class Meta:
        model = SubTask
        fields = ['title']
