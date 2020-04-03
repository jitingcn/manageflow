from django.conf.urls import url
from django.urls import include, path
from manageflow.accounts import views

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    path("login/", views.mf_login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("<str:username>/", views.profile, name="profile"),
]
