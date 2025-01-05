"""
Serializer for users.
"""

from rest_framework import serializers
from accounts.models.user_account import UserAccount
from accounts.models.invitation import Invitation


class UserSignupSerializer(serializers.Serializer):
    """Serializer for user signup."""

    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)
    invitation_id = serializers.UUIDField(required=True)

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs

    def create(self, validated_data):
        """Create a new user."""

        try:
            invitation = Invitation.objects.get(
                invitation_id=validated_data["invitation_id"]
            )
        except Invitation.DoesNotExist as exc:
            raise serializers.ValidationError(
                {"invitation_id": "Invalid invitation ID."}
            ) from exc

        user = UserAccount.objects.create_user(
            email=invitation.email,
            first_name=invitation.first_name,
            last_name=invitation.last_name,
            password=validated_data["password"],
            groups=[invitation.role],
        )
        return user

    def update(self, instance, validated_data):
        raise NotImplementedError
