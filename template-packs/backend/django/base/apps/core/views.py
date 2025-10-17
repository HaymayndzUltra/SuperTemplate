"""
Core views for {{PROJECT_NAME}}.
"""

from django.conf import settings
from django.db import connection
from django.utils import timezone
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """
    Health check endpoint for monitoring.
    """
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        health_status = {
            'status': 'healthy',
            'service': '{{PROJECT_NAME}} API',
            'version': '1.0.0',
            'timestamp': timezone.now().isoformat(),
            'checks': {}
        }
        
        # Database check
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            health_status['checks']['database'] = 'ok'
        except Exception as e:
            health_status['status'] = 'unhealthy'
            health_status['checks']['database'] = f'error: {str(e)}'
        
        # Redis check (if configured)
        if hasattr(settings, 'CACHES'):
            try:
                from django.core.cache import cache
                cache.set('health_check', 'ok', 1)
                if cache.get('health_check') == 'ok':
                    health_status['checks']['cache'] = 'ok'
                else:
                    raise Exception('Cache read/write failed')
            except Exception as e:
                health_status['status'] = 'degraded'
                health_status['checks']['cache'] = f'error: {str(e)}'
        
        status_code = status.HTTP_200_OK if health_status['status'] == 'healthy' else status.HTTP_503_SERVICE_UNAVAILABLE
        
        return Response(health_status, status=status_code)


class InfoView(APIView):
    """
    API information endpoint.
    """
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        return Response({
            'name': '{{PROJECT_NAME}} API',
            'version': '1.0.0',
            'description': '{{INDUSTRY}} {{PROJECT_TYPE}} API',
            'documentation': request.build_absolute_uri('/api/docs/'),
            'endpoints': {
                'auth': '/api/v1/auth/',
                'users': '/api/v1/users/',
                'health': '/health/',
            }
        })


class StatsView(APIView):
    """
    Basic statistics endpoint (admin only).
    """
    permission_classes = [permissions.IsAdminUser]
    
    def get(self, request):
        from django.contrib.auth import get_user_model
        from apps.users.models import UserActivity
        
        User = get_user_model()
        
        stats = {
            'users': {
                'total': User.objects.count(),
                'active': User.objects.filter(is_active=True).count(),
                'verified': User.objects.filter(is_verified=True).count(),
            },
            'activities': {
                'last_24h': UserActivity.objects.filter(
                    created_at__gte=timezone.now() - timezone.timedelta(days=1)
                ).count(),
                'last_7d': UserActivity.objects.filter(
                    created_at__gte=timezone.now() - timezone.timedelta(days=7)
                ).count(),
            }
        }
        
        return Response(stats)