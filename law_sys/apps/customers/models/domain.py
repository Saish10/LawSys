"""
This module defines the Tenant domain model for the Customer app.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2023, LawSys, Inc."

from django_tenants.models import DomainMixin


class Domain(DomainMixin):
    """
    Tenant domain model for the Customer app.
    """

    class Meta:
        """
        Meta class for the Tenant domain model.
        """
        db_table = "customer_domains"
        verbose_name = "Customer Domain"
        verbose_name_plural = "Customer Domains"
