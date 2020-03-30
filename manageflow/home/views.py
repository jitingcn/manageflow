import os

from django.shortcuts import get_object_or_404, redirect, render
from django.conf import settings
from django.http import (
    Http404,
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    JsonResponse,
)


def index(request):
    # if request.user.is_authenticated:
    #     projects = list(request.profile.projects())
    #
    #     ctx = {"page": "projects", "projects": projects}
    #     return render(request, "home/projects.haml", ctx)

    ctx = {
        "page": "welcome",
        "registration_open": settings.REGISTRATION_OPEN,
    }

    return render(request, "home/welcome.haml", ctx)


def serve_doc(request, doc="introduction"):
    path = os.path.join(settings.BASE_DIR, "templates/docs", doc + ".haml")
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
        "section": "home",
        "section": doc,
        "content": content,
        "first_line": content.split("\n")[0],
    }

    return render(request, "home/docs_single.haml", ctx)
