from django.urls import include, path

from manageflow.home import views

urlpatterns = [
    path("", views.index, name="mf-index"),
    path("docs/", views.serve_doc, name="mf-docs"),
    path("docs/<slug:doc>/", views.serve_doc, name="mf-serve-doc"),
]
