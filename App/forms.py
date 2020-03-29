from django import forms
from Accounts.models import UserProfile


class CreateNewList(forms.Form):
    name = forms.CharField(label = "Name", max_length=200)
    check = forms.BooleanField()
