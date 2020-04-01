from django.shortcuts import get_object_or_404, redirect, render
from allauth.account.forms import LoginForm
from django.contrib.auth import login, authenticate
from django.conf import settings
from .forms import CustomSignupForm
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    JsonResponse,
)


def signup(request):
    form = CustomSignupForm()
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save(request)
            return redirect('mf-index')
    ctx = {
        "page": "signup",
        "form": form,
        "registration_open": settings.REGISTRATION_OPEN,
    }
    return render(request, "accounts/signup.html", ctx)


def mf_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.login(request)
            return redirect('mf-index')
    ctx = {
        "page": "login",
        "form": form,
        "registration_open": settings.REGISTRATION_OPEN,
    }
    return render(request, "accounts/login.html", ctx)
