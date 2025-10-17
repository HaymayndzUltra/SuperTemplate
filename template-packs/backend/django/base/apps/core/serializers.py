"""
Core serializers for {{PROJECT_NAME}}.
"""

from rest_framework import serializers


class ErrorSerializer(serializers.Serializer):
    """
    Standard error response serializer.
    """
    error = serializers.CharField()
    message = serializers.CharField()
    details = serializers.DictField(required=False)
    timestamp = serializers.DateTimeField()


class SuccessSerializer(serializers.Serializer):
    """
    Standard success response serializer.
    """
    success = serializers.BooleanField(default=True)
    message = serializers.CharField()
    data = serializers.DictField(required=False)


class PaginationSerializer(serializers.Serializer):
    """
    Standard pagination response serializer.
    """
    count = serializers.IntegerField()
    next = serializers.CharField(allow_null=True)
    previous = serializers.CharField(allow_null=True)
    results = serializers.ListField()


# Add feature-specific serializers based on selected features during generation