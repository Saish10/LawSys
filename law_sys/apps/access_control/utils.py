"""
Utils for permissions and groups.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

import logging
from django.contrib.auth.models import Permission, Group

logger = logging.getLogger(__name__)


class PermissionManager:
    """Manager for permissions."""

    def __init__(self, request):
        self.request = request

    def get_permissions(self):
        """Returns a list of permissions with an optional search filter.
        If a group_id is provided, returns the permissions for that group.
        If no group_id is provided, returns all permissions.
        """
        search = self.request.query_params.get("search", None)
        group_id = self.request.query_params.get("group_id", None)
        try:
            # If group_id is provided, fetch permissions for that group
            if group_id:
                group = Group.objects.filter(id=group_id).first()
                if not group:
                    return None  # Or handle the case where group doesn't exist

                permissions = group.permissions.all()
            else:
                # If no group_id is provided, return all permissions
                permissions = Permission.objects.all()

            # Apply search filter if search parameter is provided
            if search:
                permissions = permissions.filter(name__icontains=search)

            return permissions

        except Exception as e:
            logger.error("Error getting permissions: %s", e, exc_info=True)
            return None


class RoleManager:
    """Manager for roles."""

    def __init__(self, request):
        self.request = request

    def get_roles(self, role_id=None):
        """Returns a list of roles."""
        try:
            if role_id:
                return Group.objects.filter(id=role_id).first()
            return Group.objects.all()
        except Exception as e:
            logger.error("Error getting roles: %s", e, exc_info=True)
            return None

    def delete_role(self, role_id):
        """Deletes a role by ID."""
        try:
            Group.objects.filter(id=role_id).delete()
            return True
        except Exception as e:
            logger.error("Error deleting role: %s", e, exc_info=True)
            return False

    def update_role_permissions(self, role_id):
        """Assigns permissions to a role."""
        try:
            # Get the list of permission IDs from the request
            permission_ids = self.request.data.get("permission_ids", [])

            # Ensure permissions are valid
            valid_permissions = Permission.objects.filter(
                id__in=permission_ids
            )

            # If any of the permission IDs are invalid, the lengths won't match
            if len(valid_permissions) != len(permission_ids):
                return False  # Invalid permission IDs

            # Get the role instance
            role = Group.objects.get(id=role_id)

            # Assign the valid permissions to the role
            role.permissions.set(valid_permissions)

            return True
        except Group.DoesNotExist:
            logger.error("Role with ID %s does not exist", role_id)
            return False
        except Exception as e:
            logger.error(
                "Error updating role permissions: %s", e, exc_info=True
            )
            return False
