"""
Serializers for base query
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from rest_framework import serializers


class BaseQuerySerializer(serializers.Serializer):
    """
    Serializer for base query.
    """

    page = serializers.IntegerField(required=False)
    page_size = serializers.IntegerField(required=False)
    search = serializers.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["page"].default = 1
        self.fields["page_size"].default = 10

    def create(self, validated_data):
        return NotImplementedError

    def update(self, instance, validated_data):
        return NotImplementedError


