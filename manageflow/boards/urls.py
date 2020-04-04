from django.conf.urls import url
from django.urls import include, path
from allauth.account.views import LoginView, SignupView, LogoutView
from manageflow.boards import views

urlpatterns = [
    path("", views.index, name="mf-index"),
    path("docs/", views.serve_doc, name="mf-docs"),
    path("docs/<slug:doc>/", views.serve_doc, name="mf-serve-doc"),
    path("about/", views.about, name="mf-about"),
    path("board/create/", views.create_board, name="create-board"),
    # path("", views.createBoard, name="board")
    path("task/create/", views.create_task, name="create-task"),
]
