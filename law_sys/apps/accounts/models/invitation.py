"""
This module defines the Invitation model for the Accounts app.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN."

import uuid
from base.models.base import BaseModel
from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _


class Invitation(BaseModel):
    """
    This class defines the Invitation model for the Accounts app.
    """

    email = models.EmailField(
        unique=True,
        help_text=_("Enter a valid email address (e.g., example@domain.com)."),
        verbose_name=_("Email Address"),
    )
    first_name = models.CharField(
        max_length=255,
        help_text=_("First name"),
        verbose_name=_("First Name")
    )
    last_name = models.CharField(
        max_length=255,
        help_text=_("Last Name"),
        verbose_name=_("Last Name")
    )
    role = models.ForeignKey(
        Group,
        related_name="invitations",
        help_text=_("Role"),
        verbose_name=_("Role"),
        on_delete=models.CASCADE,
    )
    token = models.UUIDField(
        default=uuid.uuid4,
        help_text=_("Invitation Token"),
        verbose_name=_("Token"),
    )
    invited_by = models.ForeignKey(
        "UserAccount",
        related_name="invitations",
        null=True,
        help_text=_("Invited By"),
        verbose_name=_("Invited By"),
        on_delete=models.CASCADE,
    )
    is_registered = models.BooleanField(
        default=False,
        help_text=_("Registered?"),
        verbose_name=_("Registered?"),
    )
    registered_date = models.DateField(
        _("Registered Date"),
        null=True,
        blank=True
    )

    class Meta:
        """
        Meta class for the Invitation model
        """

        db_table = "invitations"
        verbose_name = _("Invitation")
        verbose_name_plural = _("Invitations")

    def __str__(self):
        """
        Returns a string representation of the invitation, using the email.
        """
        return str(self.email)

    def get_invitee_name(self):
        """
        Returns the full name of the invitee,
        combining first name and last name.
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def invitee_name(self):
        """
        Returns the full name of the invitee,
        combining first name and last name.
        """
        return self.get_invitee_name()
