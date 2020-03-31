from django import forms
from django.forms import ModelForm
from .models import Board, Task

#import models here

class BoardForm(ModelForm):

    class Meta:
        model = Board
        fields = ('name', 'description')

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ('board', 'text', 'complete')