"""
This module contains the views for the Users.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN."

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from drf_yasg.utils import swagger_auto_schema
from base.utils.response import APIResponse
from accounts.serializers.users import UserSignupSerializer


class SignUpView(APIView):
    """
    View for user signup.
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_id="signup",
        tags=["Onboarding"],
        request_body=UserSignupSerializer,
    )
    def post(self, request):
        """
        Handle user signup.
        """
        serializer = UserSignupSerializer(data=request.data)
        if not serializer.is_valid():
            response = APIResponse.error(errors=serializer.errors)
            return Response(response, status=HTTP_400_BAD_REQUEST)
        user = serializer.create(serializer.validated_data)
        if not user:
            response = APIResponse.error(
                message="Something went wrong, Please try again later."
            )
            return Response(response, status=HTTP_400_BAD_REQUEST)
        response = APIResponse.success(message="User signed up successfully.")
        return Response(response, status=HTTP_200_OK)
