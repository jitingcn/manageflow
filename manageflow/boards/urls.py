from django.conf.urls import url
from django.urls import include, path
from allauth.account.views import LoginView, SignupView, LogoutView
from manageflow.boards import views

urlpatterns = [
    path("", views.index, name="mf-index"),
    path("docs/", views.serve_doc, name="mf-docs"),
    path("docs/<slug:doc>/", views.serve_doc, name="mf-serve-doc"),
    path("about/", views.about, name="mf-about"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("board/<str:board_id>/", views.board_post_detail),
    path("<str:username>/boards/", views.boards, name="mf-boards"),
    path("<str:username>/boards/create/", views.create_board, name="create-board"),
    path("<str:username>/task/create/", views.create_task, name="create-task"),
    #path("task/create/", views.create_task, name="create-task"),
]
