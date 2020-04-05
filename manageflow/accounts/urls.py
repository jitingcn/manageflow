from django.conf.urls import url
from django.urls import include, path
from manageflow.accounts import views

urlpatterns = [
    path("login/", views.mf_login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    url(r'^accounts/', include('allauth.urls')),
    path("<str:username>/", views.profile, name="profile"),
]
