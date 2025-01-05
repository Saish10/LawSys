"""Mixin for limiting fields in a serializer."""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

class FieldsMixin:
    """Mixin for limiting fields in a serializer."""
    def __init__(self, *args, **kwargs):
        only_fields = kwargs.pop("only", None)
        exclude_fields = kwargs.pop("exclude", None)

        super().__init__(*args, **kwargs)

        if only_fields:
            allowed = set(only_fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if exclude_fields:
            for field_name in exclude_fields:
                self.fields.pop(field_name, None)
