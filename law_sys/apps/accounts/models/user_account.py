"""
This module defines the UserAccount model for the Accounts app.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN."

from base.models.base import BaseModel
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserAccountManager(BaseUserManager):
    """
    Custom manager for the User model.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and returns a user with an email and password.
        """
        if not email:
            raise ValueError(_("The Email field must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Ensure password is hashed
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and returns a superuser with an email, password,
        and superuser privileges.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)


class UserAccount(BaseModel, AbstractBaseUser, PermissionsMixin):
    """
    UserAccount Model
    """

    email = models.EmailField(
        unique=True,
        help_text=_("Enter a valid email address (e.g., example@domain.com)."),
        verbose_name=_("Email Address"),
    )
    first_name = models.CharField(
        max_length=255, help_text=_("First name"), verbose_name=_("First Name")
    )
    last_name = models.CharField(
        max_length=255, help_text=_("Last Name"), verbose_name=_("Last Name")
    )
    gender = models.CharField(
        max_length=1,
        choices=[
            ("M", _("Male")),
            ("F", _("Female")),
            ("O", _("Other")),
            ("N", _("Prefer not to say")),
        ],
        help_text=_("Gender"),
        verbose_name=_("Gender"),
        null=True,
        blank=True,

    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        help_text=_("Date of Birth"),
        verbose_name=_("Date of Birth"),
    )
    phone = models.CharField(
        max_length=15,
        help_text=_("Phone number"),
        verbose_name=_("Phone Number"),
        null=True,
        blank=True,
    )
    address = models.TextField(
        help_text=_("Address"),
        verbose_name=_("Address"),
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=255,
        help_text=_("City"),
        verbose_name=_("City"),
        null=True,
        blank=True,
    )
    zip_code = models.CharField(
        max_length=10,
        help_text=_("Zip Code"),
        verbose_name=_("Zip Code"),
        null=True,
        blank=True,
    )
    state = models.ForeignKey(
        "base.State",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text=_("State"),
        verbose_name=_("State"),
        related_name="users",
    )
    country = models.ForeignKey(
        "base.Country",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text=_("Country"),
        verbose_name=_("Country"),
        related_name="users",
    )
    is_staff = models.BooleanField(
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
        verbose_name=_("Staff status"),
    )
    objects = UserAccountManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        """
        Returns a string representation of the user account, using the email.
        """
        return str(self.email)

    class Meta:
        """
        Meta options for the UserAccount model
        """

        db_table = "user_accounts"
        verbose_name = _("User Account")
        verbose_name_plural = _("User Accounts")

    def get_full_name(self):
        """
        Returns the full name of the user, combining first name and last name.
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        """
        Returns the full name of the user, combining first name and last name.
        """
        return self.get_full_name()
