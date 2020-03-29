from django.urls import path
from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("faq/", views.faqs, name="FAQs"),
    path("Loggedin/", views.loggedin, name="Loggedin"),
]