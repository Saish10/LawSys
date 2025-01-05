"""
URLs for the accounts app
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN."

from django.urls import path
from accounts.views.auth import LoginView, LogoutView
from accounts.views.signup import SignUpView
from accounts.views.invitations import InvitationViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'invitation', InvitationViewSet, basename="invitation")

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

] + router.urls
