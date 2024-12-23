"""
This module defines the State model for apps.
"""

from base.models.base import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _

class State(BaseModel):
    """
    State Model
    """

    name = models.CharField(
        max_length=255,
        help_text=_("State name"),
        verbose_name=_("State Name"),
    )
    code = models.CharField(
        max_length=5,
        help_text=_("State code"),
        verbose_name=_("State Code"),
    )
    country = models.ForeignKey(
        "Country",
        on_delete=models.CASCADE,
        related_name="states",
        verbose_name=_("Country"),
        help_text=_("Country"),
    )

    class Meta:
        """
        Meta class for the State model
        """

        db_table = "states"
        verbose_name = _("State")
        verbose_name_plural = _("States")

    def __str__(self):
        """
        Returns a string representation of the state, using the name.
        """
        return str(self.name)
