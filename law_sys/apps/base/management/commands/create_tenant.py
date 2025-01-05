"""
This module defines a Django management command to create tenants and their
associated domains.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from customers.models.customer import Customer
from customers.models.domain import Domain
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    """
    Django management command to create tenants and their associated domains.
    """

    help = "Create tenants and their associated domains interactively"

    def handle(self, *args, **kwargs):
        """Create tenants and their associated domains interactively."""
        schema_name = input(
            "Enter schema name (e.g. 'tenant1', or 'public'): "
        ).strip()
        email = input("Enter tenant email: ").strip()
        password = input("Enter tenant password: ").strip()

        if schema_name == "public":
            self.create_public_tenant(email)
            self.create_superuser(
                email=email, password=password, schema_name=schema_name
            )
        else:
            # For non-public tenants, ask for tenant-specific details
            tenant_name = input("Enter tenant name: ").strip()
            domain = input(
                "Enter domain (e.g. 'tenant1.example.com'): "
            ).strip()
            is_primary = (
                input("Is this the primary domain? (y/n): ").strip().lower()
                == "y"
            )
            self.create_tenant(
                tenant_name, schema_name, email, domain, is_primary
            )
            self.create_superuser(
                email=email, password=password, schema_name=schema_name
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Tenant & domain created completed for schema: {schema_name}"
            )
        )

    def create_public_tenant(self, email):
        """Create the public tenant with default domain if it doesn't exist."""
        try:
            public_tenant = Customer.objects.get(schema_name="public")
            self.stdout.write(
                self.style.SUCCESS("Public tenant already exists.")
            )
        except ObjectDoesNotExist:
            public_tenant = Customer.objects.create(
                schema_name="public",
                name="Owner Tenant",
                email=email,
            )
            Domain.objects.create(
                domain="localhost", tenant=public_tenant, is_primary=True
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully created public tenant with domain:localhost."
                )
            )

    def create_tenant(
        self, tenant_name, schema_name, email, domain, is_primary
    ):
        """Create a new tenant and associate it with a domain."""
        try:
            tenant = Customer.objects.create(
                schema_name=schema_name,
                name=tenant_name,
                email=email,
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created tenant: {tenant_name}"
                )
            )
        except ValidationError as e:
            self.stderr.write(f"Error creating tenant: {e}")
            return

        # Create and add domain to the tenant
        self.create_or_update_domain(tenant, domain, is_primary)

    def create_or_update_domain(self, tenant, domain, is_primary):
        """Create or update the domain for the given tenant."""
        try:
            _, created = Domain.objects.get_or_create(
                domain=domain,
                tenant=tenant,
                defaults={"is_primary": is_primary},
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully added domain '{domain}' for tenant '{tenant.name}'"
                    )
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Domain '{domain}' already exists for tenant '{tenant.name}'"
                    )
                )
        except Exception as e:
            self.stderr.write(f"Error creating or updating domain: {e}")

    def create_superuser(self, email, password, schema_name="public"):
        """Creates and returns a superuser with an email, password, and superuser privileges."""
        try:
            # Switch to the tenant's schema if it's not the public schema
            if schema_name != "public":
                self.set_schema(schema_name)

            UserAccount = get_user_model()  # Dynamically get the user model
            # Check if the superuser already exists to avoid duplicates
            if UserAccount.objects.filter(email=email).exists():
                self.stdout.write(
                    self.style.WARNING(
                        f"Superuser with email {email} already exists."
                    )
                )
                return

            superuser = UserAccount.objects.create_superuser(
                email=email,
                password=password,
                first_name="Superuser",
                last_name="",
            )
            self.stdout.write(
                self.style.SUCCESS(f"Superuser created: {superuser.email}")
            )

        except Exception as e:
            self.stderr.write(f"Error creating superuser: {e}")
        finally:
            # Ensure that the schema is reset to the public schema
            if schema_name != "public":
                self.set_schema("public")

    def set_schema(self, schema_name):
        """Sets the current schema for the database connection."""
        # This assumes you're using a multi-tenant schema-based approach
        connection.set_schema(schema_name)
        self.stdout.write(
            self.style.SUCCESS(f"Switched to schema '{schema_name}'")
        )
