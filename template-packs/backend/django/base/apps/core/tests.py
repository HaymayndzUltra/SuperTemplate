"""
Core tests for {{PROJECT_NAME}}.
"""

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()


class HealthCheckTestCase(APITestCase):
    """Test case for health check endpoint."""
    
    def test_health_check(self):
        """Test health check returns healthy status."""
        url = reverse('health_check:health_check_home')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('status', response.data)
        self.assertEqual(response.data['status'], 'healthy')
        self.assertIn('checks', response.data)


class InfoViewTestCase(APITestCase):
    """Test case for info endpoint."""
    
    def test_info_endpoint(self):
        """Test info endpoint returns API information."""
        url = reverse('core:info')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('name', response.data)
        self.assertIn('version', response.data)
        self.assertIn('endpoints', response.data)
        self.assertEqual(response.data['name'], '{{PROJECT_NAME}} API')


class StatsViewTestCase(APITestCase):
    """Test case for stats endpoint."""
    
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='AdminPass123!'
        )
        
        self.regular_user = User.objects.create_user(
            username='user',
            email='user@example.com',
            password='UserPass123!'
        )
    
    def test_stats_requires_admin(self):
        """Test stats endpoint requires admin permission."""
        url = reverse('core:stats')
        
        # Unauthenticated
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        # Regular user
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Admin user
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_stats_content(self):
        """Test stats endpoint returns correct statistics."""
        self.client.force_authenticate(user=self.admin_user)
        
        url = reverse('core:stats')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('activities', response.data)
        self.assertEqual(response.data['users']['total'], 2)  # admin + regular user