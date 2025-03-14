from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','content','completed']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Enter Task Title'}),
            'content' : forms.TextInput(attrs={'class' : 'form-control' ,'rows' : 4, 'placeholder' : 'Enter Task Details'}),
            'completed' : forms.CheckboxInput(attrs={'class'  : 'form-check-input'})
        }

