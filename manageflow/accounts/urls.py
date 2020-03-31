from django.conf.urls import url
from django.urls import include, path
from allauth.account.views import LoginView, SignupView, LogoutView

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    path("login/", LoginView.as_view(), name="login"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
]