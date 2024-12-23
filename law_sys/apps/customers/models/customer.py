"""
    Customer Model
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from django_tenants.models import TenantMixin


class Customer(TenantMixin):
    """
    Customer Model
    """

    schema_name = models.CharField(max_length=100, unique=True)
    name = models.CharField(
        max_length=255,
        help_text=_("Customer name"),
        verbose_name=_("Customer Name"),
    )
    email = models.EmailField(
        unique=True,
        db_index=True,
        verbose_name=_("Email Address"),
        help_text=_("Enter a valid email address (e.g., example@domain.com).")
    )
    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        help_text=_("Customer phone number"),
        verbose_name=_("Phone Number"),
    )
    address = models.TextField(
        blank=True,
        null=True,
        help_text=_("Customer address"),
        verbose_name=_("Address")
    )

    def __str__(self):
        return str(self.name)

    class Meta:
        """
        Meta class
        """

        db_table = "customers"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
