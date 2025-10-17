"""
User views for {{PROJECT_NAME}}.
"""

from django.contrib.auth import get_user_model
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import UserActivity
from .serializers import (
    UserActivitySerializer,
    UserDetailSerializer,
    UserListSerializer,
)

User = get_user_model()


class IsOwnerOrAdmin(permissions.BasePermission):
    """Permission to only allow owners or admins to edit."""
    
    def has_object_permission(self, request, view, obj):
        # Read permissions for authenticated users
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        
        # Write permissions for owner or admin
        return obj == request.user or request.user.is_staff


class UserViewSet(ModelViewSet):
    """
    ViewSet for user management.
    """
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering_fields = ['created_at', 'last_login', 'username', 'email']
    ordering = ['-created_at']
    
    def get_queryset(self):
        queryset = User.objects.select_related('profile')
        
        # Non-admin users can only see active users
        if not self.request.user.is_staff:
            queryset = queryset.filter(is_active=True)
        
        # Filter by query parameters
        is_active = self.request.query_params.get('is_active')
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == 'true')
        
        is_verified = self.request.query_params.get('is_verified')
        if is_verified is not None:
            queryset = queryset.filter(is_verified=is_verified.lower() == 'true')
        
        return queryset
    
    def get_serializer_class(self):
        if self.action == 'list':
            return UserListSerializer
        return UserDetailSerializer
    
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwnerOrAdmin]
        elif self.action == 'create':
            # Only admins can create users via API
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()
    
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        """Activate a user account (admin only)."""
        if not request.user.is_staff:
            return Response(
                {"detail": "You don't have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        user = self.get_object()
        user.is_active = True
        user.save()
        
        return Response(
            {"detail": "User activated successfully."},
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        """Deactivate a user account (admin only)."""
        if not request.user.is_staff:
            return Response(
                {"detail": "You don't have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        user = self.get_object()
        user.is_active = False
        user.save()
        
        return Response(
            {"detail": "User deactivated successfully."},
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['get'])
    def activities(self, request, pk=None):
        """Get user's activity history."""
        user = self.get_object()
        
        # Only user themselves or admin can view activities
        if user != request.user and not request.user.is_staff:
            return Response(
                {"detail": "You don't have permission to view this user's activities."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        activities = UserActivity.objects.filter(user=user)
        
        # Apply filters
        action = request.query_params.get('action')
        if action:
            activities = activities.filter(action=action)
        
        resource = request.query_params.get('resource')
        if resource:
            activities = activities.filter(resource=resource)
        
        # Pagination
        page = self.paginate_queryset(activities)
        if page is not None:
            serializer = UserActivitySerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        
        serializer = UserActivitySerializer(activities, many=True)
        return Response(serializer.data)


class UserSearchView(generics.ListAPIView):
    """
    Search users by various criteria.
    """
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        
        if not query:
            return User.objects.none()
        
        return User.objects.filter(
            Q(username__icontains=query) |
            Q(email__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        ).filter(is_active=True)[:20]  # Limit results