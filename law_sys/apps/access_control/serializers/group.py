"""
Serializers for groups.
"""

from django.contrib.auth.models import Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for groups."""

    name = serializers.CharField(required=True)

    class Meta:
        """Meta class for group serializer."""

        model = Group
        fields = ["id", "name"]
        read_only_fields = ["id",]

    def validate_name(self, value):
        """
        Ensure the group name is case-insensitive unique.
        Normalize name to lowercase and check if the same name already exists.
        """
        name = (
            value.strip().title()
        )  # Capitalize the first letter of each word

        if Group.objects.filter(name__iexact=name).exists():
            raise serializers.ValidationError(
                f"A role with the name '{name}' already exists."
            )

        return name

