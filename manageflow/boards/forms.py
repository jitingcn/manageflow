from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import Group
from .models import Board, Task

#import models here

class BoardForm(ModelForm):

    class Meta:
        model = Board
        fields = ('name', 'description')

class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ('board', 'text', 'complete', 'assigned_to')