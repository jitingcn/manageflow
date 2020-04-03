from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import Group
from .models import Board

#import models here

class CreateNewBoard(ModelForm):
    name = forms.CharField(max_length=200, help_text="Please enter the Board name")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Board
        fields = ('name',)




