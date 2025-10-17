"""
User serializers for {{PROJECT_NAME}}.
"""

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import UserActivity, UserProfile

User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profiles."""
    
    class Meta:
        model = UserProfile
        fields = [
            'job_title', 'department', 'company',
            'timezone', 'language', 'notifications_enabled',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


class UserListSerializer(serializers.ModelSerializer):
    """Serializer for user list view."""
    
    profile = UserProfileSerializer(read_only=True)
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'full_name',
            'is_verified', 'is_active', 'last_login',
            'created_at', 'profile'
        ]
        read_only_fields = ['id', 'created_at']
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or obj.username


class UserDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for user."""
    
    profile = UserProfileSerializer()
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'full_name', 'is_verified', 'is_active', 'is_staff',
            'phone_number', 'date_of_birth', 'bio', 'avatar',
            'last_login', 'last_activity', 'created_at', 'updated_at',
            'profile'
        ]
        read_only_fields = [
            'id', 'is_verified', 'is_staff', 'last_login',
            'last_activity', 'created_at', 'updated_at'
        ]
    
    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip() or obj.username
    
    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        
        # Update user fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # Update or create profile
        profile, created = UserProfile.objects.get_or_create(user=instance)
        for attr, value in profile_data.items():
            setattr(profile, attr, value)
        profile.save()
        
        return instance


class UserActivitySerializer(serializers.ModelSerializer):
    """Serializer for user activities."""
    
    user_email = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = UserActivity
        fields = [
            'id', 'user', 'user_email', 'action', 'resource',
            'resource_id', 'ip_address', 'user_agent', 'metadata',
            'created_at'
        ]
        read_only_fields = ['id', 'user', 'created_at']