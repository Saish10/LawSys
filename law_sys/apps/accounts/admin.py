"""
This module defines the admin interface for the Accounts app.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN."

from django.contrib import admin

from accounts.models.user_account import UserAccount
from accounts.models.invitation import Invitation


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    """
    Admin interface for the UserAccount model.
    """

    list_display = [
        "internal_id",
        "email",
        "full_name",
        "is_active",
    ]
    search_fields = [
        "email",
        "full_name",
        "internal_id",
    ]
    list_filter = ["is_active", "groups"]
    filter_horizontal = ("groups",)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        if db_field.name == "groups":
            qs = kwargs.get("queryset", db_field.remote_field.model.objects)
            kwargs["queryset"] = qs

        return super().formfield_for_manytomany(
            db_field, request=request, **kwargs
        )


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    """
    Admin interface for the Invitation model.
    """

    list_display = [
        "email",
        "invitee_name",
        "role",
    ]
    search_fields = [
        "email",
        "first_name",
        "last_name",
    ]
    list_filter = ["role", "is_active", "is_registered"]
