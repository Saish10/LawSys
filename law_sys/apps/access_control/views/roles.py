"""
Views for roles
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN."

from base.utils.pagination import StandardPagination
from base.utils.response import APIResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_201_CREATED
)
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from access_control.utils import RoleManager
from access_control.serializers.group import GroupSerializer


class RoleViewSet(ViewSet):
    """
    View for listing roles
    """

    permission_classes = [AllowAny]
    serializer_class = GroupSerializer
    lookup_field = "role_id"

    @swagger_auto_schema(
        operation_id="role list",
        operation_description="Returns a list of roles.",
        operation_summary="Role list",
        tags=["Roles"],
    )
    def list(self, request):
        """
        List roles with search and pagination.
        """
        roles = RoleManager(request).get_roles()
        if roles is None:
            response = APIResponse.success(
                message="Roles list is empty.", data=[]
            )
            return Response(response, status=HTTP_200_OK)
        data = StandardPagination(request).paginate(
            roles, self.serializer_class
        )
        response = APIResponse.success(
            message="Roles list retrieved successfully.", data=data
        )
        return Response(response, status=HTTP_200_OK)

    @swagger_auto_schema(
        operation_id="create role",
        operation_description="Create a new role.",
        operation_summary="Create role",
        tags=["Roles"],
        request_body=GroupSerializer,
    )
    def create(self, request):
        """
        Create a new role.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = APIResponse.success(
                message="Role created successfully.", data=[]
            )
            return Response(response, status=HTTP_201_CREATED)
        response = APIResponse.error(errors=serializer.errors)
        return Response(response, status=HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id="delete role",
        operation_description="Delete a role by ID.",
        operation_summary="Delete role",
        tags=["Roles"],
    )
    def destroy(self, request, role_id=None):
        """
        Delete a role by ID.
        """
        RoleManager(request).delete_role(role_id)
        response = APIResponse.success(
            message="Role deleted successfully.", data=[]
        )
        return Response(response, status=HTTP_200_OK)

    @swagger_auto_schema(
        operation_id="update role permissions",
        operation_description="Update an existing role's permissions.",
        operation_summary="Update role permissions",
        tags=["Roles"],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "permission_ids": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(type=openapi.TYPE_INTEGER),
                )
            },
        )
    )
    @action(detail=True, methods=["put"], url_path="assign-permissions")
    def assign_permissions(self, request, role_id):
        """
        Update an existing role's permissions.
        """
        is_success = RoleManager(request).update_role_permissions(role_id)
        if not is_success:
            response = APIResponse.error(
                message="Something went wrong, Please try again later."
            )
            return Response(response, status=HTTP_400_BAD_REQUEST)
        response = APIResponse.success(
            message="Role permissions updated successfully.", data=[]
        )
        return Response(response, status=HTTP_200_OK)
