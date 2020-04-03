from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import Group
from .models import Board, Task


class CreateNewBoard(ModelForm):
    name = forms.CharField(max_length=200, help_text="Please enter the Board name")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Board
        fields = ('name',)


class CreateNewTask(ModelForm):
    text = forms.CharField(max_length=200, help_text="please enter a task")
    complete = forms.BooleanField()
    assigned_to = forms.CharField(max_length=30, help_text="Assigned to :")

    class Meta:
        model = Task
        fields = ('board', 'text', 'complete', 'assigned_to')
