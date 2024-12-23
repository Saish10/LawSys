"""
This module defines the admin interface for the base app.
"""
__author__ = 'Saish Naik'
__copyright__ = 'Copyright 2024, SN'

from django.contrib import admin
from base.models.country import Country
from base.models.state import State


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    """
    Admin interface for the Country model.
    """

    list_display = (
        "name",
        "numeric_code",
        "alpha2_code",
        "alpha3_code",
        "isd_code",
    )
    search_fields = (
        "name",
        "numeric_code",
        "alpha2_code",
        "alpha3_code",
        "isd_code",
    )


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    """
    Admin interface for the State model.
    """

    list_display = ("name", "code", "country")
    search_fields = ("name", "code", "country__name")
