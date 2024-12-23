"""
URLs for the accounts app
"""
from django.urls import path
from accounts.views.auth import (
    LoginView, LogoutView
)
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]
