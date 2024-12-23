"""
Views for user authentication.
"""

from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import (
    Token,
)
from rest_framework.permissions import (
    AllowAny,
)
from base.utils.response import APIResponse
from accounts.serializers.auth import LoginSerializer
from drf_yasg.utils import swagger_auto_schema


class LoginView(APIView):
    """
    View for user login.
    """

    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_id="login",
        tags=["Auth"],
        request_body=LoginSerializer,
    )
    def post(self, request):
        """
        Handle user login.
        """
        serializer = LoginSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, _ = Token.objects.get_or_create(user=user)
            response = APIResponse.success(
                message="User logged in successfully",
                data={"token": token.key},
            )
            return Response(response, status=HTTP_200_OK)

        response = APIResponse.error(errors=serializer.errors)
        return Response(response, status=HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    View for user logout.
    """

    @swagger_auto_schema(
        operation_id="logout",
        tags=["Auth"],
    )
    def post(self, request):
        """
        Handle user logout.
        """
        request.user.auth_token.delete()
        response = APIResponse.success(message="User logged out successfully")
        return Response(response, status=HTTP_200_OK)
