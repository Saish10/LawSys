"""
View for listing permissions
"""

from access_control.serializers.permission import (
    PermissionQuerySerializer,
    PermissionSerializer,
)
from access_control.utils import PermissionManager
from base.utils.response import APIResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import ViewSet


class PermissionViewSet(ViewSet):
    """
    View for listing permissions
    """

    permission_classes = [AllowAny]
    serializer_class = PermissionSerializer

    @swagger_auto_schema(
        operation_id="permission list",
        operation_description="Returns a list of permissions.",
        operation_summary="Permission list",
        tags=["Permissions"],
        query_serializer=PermissionQuerySerializer,
    )
    def list(self, request):
        """
        List permissions with search and pagination.
        """
        permissions = PermissionManager(request).get_permissions()
        data = self.serializer_class(permissions, many=True).data
        response = APIResponse.success(
            message="Permissions list retrieved successfully.", data=data
        )
        return Response(response, status=HTTP_200_OK)
