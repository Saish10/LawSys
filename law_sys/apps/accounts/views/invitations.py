"""
This module contains the views for the Invitations.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN."


from accounts.serializers.invitations import InvitationSerializer
from accounts.utils import InvitationManager
from base.utils.pagination import StandardPagination
from base.utils.response import APIResponse
from drf_yasg.utils import swagger_auto_schema
# from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.viewsets import ViewSet


class InvitationViewSet(ViewSet):
    """
    View for invitations.
    """

    serializer_class = InvitationSerializer

    @swagger_auto_schema(
        operation_id="invite",
        operation_description="Invite a user.",
        operation_summary="Invite users",
        tags=["Onboarding"],
        request_body=InvitationSerializer,
    )
    def create(self, request):
        """
        Handle invitation.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = APIResponse.success(
                message="Invitation sent successfully."
            )
            return Response(response, status=HTTP_201_CREATED)
        response = APIResponse.error(errors=serializer.errors)
        return Response(response, status=HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_id="invitation list",
        operation_description="Returns a list of invitations.",
        operation_summary="Invitation list",
        tags=["Onboarding"],
    )
    def list(self, request):
        """
        List invitations.
        """
        queryset = InvitationManager(request).get_invitations()
        if queryset is None:
            response = APIResponse.success(
                "Invitations list is empty.", data=[]
            )
            return Response(response, status=HTTP_200_OK)
        data = StandardPagination(request).paginate(
            queryset, serializer_class=self.serializer_class
        )
        response = APIResponse.success(
            message="Invitations list retrieved successfully.", data=data
        )
        return Response(response, status=HTTP_200_OK)
