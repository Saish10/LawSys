"""
This module defines the BaseModel model for the all apps.
"""

import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    """
    Base Model
    """
    internal_id = models.UUIDField(
        unique=True,
        default=uuid.uuid4,
        editable=False,
        help_text=_('Internal ID'),
        verbose_name=_("Internal ID"),
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_("Indicates whether the object is active or not"),
        verbose_name=_("Active"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("The date and time when the object was created"),
        verbose_name=_("Created At"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=_("The date and time when the object was last updated"),
        verbose_name=_("Updated At"),
    )

    class Meta:
        """
        Meta class
        """
        abstract = True
