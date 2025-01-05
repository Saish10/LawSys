"""
URLs for the accounts app
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN."

from rest_framework.routers import DefaultRouter
from access_control.views.permissions import PermissionViewSet
from access_control.views.roles import RoleViewSet

router = DefaultRouter()
router.register(r"permissions", PermissionViewSet, basename="permissions")
router.register(r"roles", RoleViewSet, basename="roles")

urlpatterns = [] + router.urls
