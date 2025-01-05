"""
Serializers for permissions.
"""
from django.contrib.auth.models import Permission
from rest_framework import serializers



class PermissionSerializer(serializers.ModelSerializer):
    """Serializer for groups."""
    class Meta:
        """Meta class for the group serializer."""
        model = Permission
        fields = ["id", "name", "codename"]


class PermissionQuerySerializer(serializers.Serializer):
    """
    Serializer for permission query.
    """
    search = serializers.CharField(required=False)
    role_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return NotImplemented

    def update(self, instance, validated_data):
        return NotImplemented
