from django import forms
from allauth.account.forms import SignupForm
from django.utils.translation import gettext_lazy as _


class CustomSignupForm(SignupForm):
    email = forms.EmailField(label=_("E-mail"),
                             required=True,
                             widget=forms.TextInput(
                                 attrs={'type': 'email',
                                        'placeholder': _('E-mail address')}))
    nickname = forms.CharField(label=_('Nickname (optional)'),
                               required=False,
                               widget=forms.TextInput(
                                   attrs={'type': 'text',
                                          'placeholder': _('Nickname (optional)')}
                               ))

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.nickname = self.cleaned_data['nickname']
        user.save()
        return user
