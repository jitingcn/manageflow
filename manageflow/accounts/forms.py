from django import forms
from manageflow.accounts.models import UserManager, User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = UserManager
        fields = ('username', 'email', 'password', 'is_staff', 'is_superuser')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','nickname', 'picture',)