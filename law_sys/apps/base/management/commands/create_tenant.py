"""
This module defines a Django management command to create tenants and their
associated domains.
"""

from customers.models import Customer, Domain
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Django management command to create tenants and their associated domains.
    """

    help = "Create tenants and their associated domains interactively"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **kwargs):
        """Create tenants and their associated domains interactively."""
        tenant_name = input("Enter tenant name: ")
        schema_name = input(
            "Enter schema name (e.g. 'tenant1', or 'public'): "
        )
        email = input("Enter tenant email: ")
        domain = input("Enter domain (e.g. 'tenant1.example.com'): ")
        is_primary = (
            input("Is this the primary domain? (y/n): ").strip().lower() == "y"
        )

        if schema_name == "public":
            self.create_public_tenant()
        else:
            self.create_tenant(
                tenant_name, schema_name, email, domain, is_primary
            )

        self.stdout.write(
            self.style.SUCCESS("Tenant and domain creation completed!")
        )

    def create_public_tenant(self):
        """Create the public tenant with default domain if it doesn't exist."""
        try:
            public_tenant = Customer.objects.get(schema_name="public")
            self.stdout.write(
                self.style.SUCCESS("Public tenant already exists.")
            )
        except ObjectDoesNotExist:
            public_tenant = Customer.objects.create(
                schema_name="public",
                name="LawSys",
                email="public@lawsys.com",
            )
            Domain.objects.create(
                domain="localhost", tenant=public_tenant, is_primary=True
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "Successfully created public tenant with domain localhost"
                )
            )

    def create_tenant(
        self, tenant_name, schema_name, email, domain, is_primary
    ):
        """Create a new tenant and associate it with a domain."""
        # Create the tenant (normal tenant)
        tenant = Customer(
            schema_name=schema_name,
            name=tenant_name,
            email=email,
        )
        tenant.save()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully created tenant: {tenant_name}")
        )

        # Create and add domain to the tenant
        _, created = Domain.objects.get_or_create(
            domain=domain, tenant=tenant, defaults={"is_primary": is_primary}
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully added domain {domain} for tenant {tenant_name}"
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f"Domain {domain} already exists for tenant {tenant_name}"
                )
            )
