"""
Serializers for the invitations.
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN."

from rest_framework import serializers
from accounts.models.invitation import Invitation
from django.contrib.auth.models import Group


class InvitationSerializer(serializers.ModelSerializer):
    """Serializer for invitations."""

    class Meta:
        """Meta class for the invitation serializer."""
        model = Invitation
        fields = (
            "email",
            "first_name",
            "last_name",
            "role",

        )
        read_only_fields = ("internal_id", "created_at")

    def validate(self, attrs):
        """Validate the invitation."""
        if Invitation.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError(
                {"email": "Email already exists."}
            )

        if Group.objects.filter(id=attrs["role"]).exists() is False:
            raise serializers.ValidationError({"role_id": "Invalid role ID."})
        return attrs
