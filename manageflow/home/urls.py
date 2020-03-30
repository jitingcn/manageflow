from django.conf.urls import url
from django.urls import include, path

from manageflow.home import views

urlpatterns = [
    path("", views.index, name="mf-index"),
    url(r'^accounts/', include('allauth.urls')),
    path("docs/", views.serve_doc, name="mf-docs"),
    path("docs/<slug:doc>/", views.serve_doc, name="mf-serve-doc"),
]
