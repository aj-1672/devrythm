from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # your views.py in the core app

urlpatterns = [
    path("", views.home, name="home"),  # root URL, calls home view
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path("home/", views.landing, name="landing"),  # landing page after login
]
