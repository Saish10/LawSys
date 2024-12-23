"""
This module defines the Country model for apps.
"""

from base.models.base import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Country(BaseModel):
    """
    Country Model
    """

    name = models.CharField(
        max_length=255,
        help_text=_("Country name"),
        verbose_name=_("Country Name"),
    )
    numeric_code = models.CharField(
        max_length=10,
        help_text=_("Country numeric code"),
        verbose_name=_("Country Numeric Code"),
    )

    alpha2_code = models.CharField(
        max_length=2,
        help_text=_("country alpha2 code"),
        verbose_name=_("Country Alpha2 Code"),
    )

    alpha3_code = models.CharField(
        max_length=3,
        help_text=_("Country alpha3 code"),
        verbose_name=_("Country Alpha3 Code"),
    )

    isd_code = models.CharField(
        max_length=4,
        help_text=_("Country alpha3 code"),
        verbose_name=_("Country ISD Code"),
    )

    class Meta:
        """
        Meta class for the Country model
        """

        db_table = "countries"
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def __str__(self):
        """
        Returns a string representation of the country, using the name.
        """
        return str(self.name)
