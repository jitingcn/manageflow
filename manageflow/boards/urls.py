from django.conf.urls import url
from django.urls import include, path
from allauth.account.views import LoginView, SignupView, LogoutView
from manageflow.boards import views

urlpatterns = [
    path("", views.index, name="mf-index"),
    path("docs/", views.serve_doc, name="mf-docs"),
    path("docs/<slug:doc>/", views.serve_doc, name="mf-serve-doc"),
<<<<<<< HEAD

=======
    path("about/", views.about, name="mf-about")
>>>>>>> 89d02adb2b2f0b54e80cf602ce61253646d10516
]
