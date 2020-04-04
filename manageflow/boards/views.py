import os

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    JsonResponse,
    HttpResponseRedirect)
from .forms import CreateNewBoard, CreateNewTask
from .models import Board, Task


def index(request):
    if request.user.is_authenticated:
        # projects = list(request.profile.projects())
        #
        # ctx = {"page": "projects", "projects": projects}
        return redirect(f"/{request.user.get_username()}/")

    ctx = {
        "page": "welcome",
        "registration_open": settings.REGISTRATION_OPEN,
    }
    return render(request, "boards/welcome.html", ctx)


def serve_doc(request, doc="introduction"):
    path = os.path.join(settings.BASE_DIR, "templates/docs", doc + ".html")
    if not os.path.exists(path):
        raise Http404("not found")

    replaces = {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_ROOT": settings.SITE_ROOT,
        "IMG_URL": os.path.join(settings.STATIC_URL, "img/docs"),
    }

    content = open(path, "r", encoding="utf-8").read()
    for placeholder, value in replaces.items():
        content = content.replace(placeholder, value)

    ctx = {
        "page": "docs",
        "section": "boards",
        "section": doc,
        "content": content,
        "first_line": content.split("\n")[0],
        "registration_open": settings.REGISTRATION_OPEN,
    }

    return render(request, "boards/docs.html", ctx)


def about(request):
    ctx = {
        "page": "about",
        "registration_open": settings.REGISTRATION_OPEN,
    }

    return render(request, "about.html", ctx)


@login_required
def create_Board(request):
    form = CreateNewBoard()

    if request.method == "POST":
        form = CreateNewBoard(request.POST)

        if form.is_valid():
            temp = form.save(commit=False)
            temp.save()
            return redirect('/dashboard/')

    return render(request, 'boards/create_board.html', {'form': form})

@login_required
def dashboard(request):
    username = user.get_username()
    return HttpResponse("Howdy" + username)

@login_required
def createTask(request, board_id):
    if request.method == "POST":
        form = CreateNewTask(request.POST)

        if form.is_valid():
            pass
    else:
        form = CreateNewTask()
    return render(request, 'boards/task.html', {'form': form})

def board_post_detail(request, board_id):
    obj = get_object_or_404(Board, id=board_id)
    context = {"object": obj}
    return render(request, 'boards/board_post_detail.html', context)

@login_required
def createTask(request):
    if request.method == "POST":
        form = CreateNewTask(request.POST)

        if form.is_valid():
            pass
    else:
        form = CreateNewTask()
    return render(request, 'boards/task.html', {'form': form})

def board_post_detail(request, board_id):
    obj = get_object_or_404(Board, id=board_id)
    context= {"object": obj}
    return render(request, 'boards/board_post_detail.html', context)

