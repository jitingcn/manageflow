from django import forms
from django.forms import ModelForm
from .models import Board, Task

#import models here


class CreateNewBoard(ModelForm):
    name = forms.CharField(max_length=200,
                           widget=forms.TextInput(attrs={'type': 'name',
                                                         'placeholder': "Please enter the Board name"}))
    description = forms.CharField(widget=forms.TextInput(attrs={'type': 'description',
                                                                'placeholder': "Please enter the Board description"}),
                                  required=False)
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Board
        fields = ('name', 'description')



class CreateNewTask(ModelForm):
    text = forms.CharField(max_length=300, help_text="Please enter a task")
    assigned_to = forms.CharField(max_length=30, help_text="Assigned to")
    complete = forms.BooleanField(initial=False, required=False, help_text="complete?")

    class Meta:
        model = Task
        fields = ('board', 'text', 'complete', 'assigned_to')