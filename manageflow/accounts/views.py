from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from allauth.account.forms import LoginForm
from allauth.account.views import LogoutView
from django.contrib.auth import login
from django.conf import settings
from django.contrib.auth import get_user_model
from .forms import CustomSignupForm
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    JsonResponse,
)

from .models import Project, Member, UserProfile, User


def signup(request):
    form = CustomSignupForm()
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            UserProfile.objects.for_user(user=user)
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


class CustomLogoutView(LogoutView):
    template_name = "accounts/logout.html"


logout = CustomLogoutView.as_view()


@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    if username == request.user.get_username():
        user_profile = UserProfile.owner_profile
    else:
        user_profile = user.profile
    nickname = user.nickname or username
    ctx = {
        "page": "profile",
        "username": username,
        "nickname": nickname,
        "profile": user_profile,
        "user": user,
    }

    if request.method == "POST" and username == request.user.get_username():
        if "change_email" in request.POST:
            user_profile.send_change_email_link()
            return redirect(f"{username}/")
        elif "set_password" in request.POST:
            user_profile.send_set_password_link()
            return redirect(f"{username}/")
        elif "leave_project" in request.POST:
            code = request.POST["code"]
            try:
                project = Project.objects.get(code=code, member_user=request.user)
            except Project.DoesNotExist:
                return HttpResponseBadRequest()

            Member.objects.filter(project=project, user=request.user).delete()

            ctx["left_project"] = project
            ctx["projects_status"] = "info"

    return render(request, "accounts/profile.html", ctx)
