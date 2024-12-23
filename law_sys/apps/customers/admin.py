"""
This module defines the admin interface for the Customer app.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2023, LawSys, Inc."

from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from customers.models.customer import Customer
from customers.models.domain import Domain


@admin.register(Customer)
class CustomerAdmin(TenantAdminMixin, admin.ModelAdmin):
    """Admin interface for the Customer model."""

    list_display = ("name", "schema_name", "email")
    search_fields = ("name", "email")
    readonly_fields = ("schema_name",)

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    """Admin interface for the Domain model."""

    list_display = ("domain", "tenant", "is_primary")
    search_fields = ("domain", "tenant__name")
