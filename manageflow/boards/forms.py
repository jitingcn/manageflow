from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import Group
from .models import Board, Task

#import models here


class CreateNewBoard(ModelForm):
    name = forms.CharField(max_length=200, help_text="Please enter the Board name")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Board
        fields = ('name', )

class CreateNewTask(ModelForm):
    text = forms.CharField(max_length=300, help_text="Please enter a task")
    assigned_to = forms.CharField(max_length=30, help_text= "Assigned to")
    complete = forms.BooleanField(help_text="complete?")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Task
        fields = ( 'text', 'assigned_to', 'complete')



