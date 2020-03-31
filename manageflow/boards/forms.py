from django import forms
from .models import board

#import models here

class createBoard(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    pass
