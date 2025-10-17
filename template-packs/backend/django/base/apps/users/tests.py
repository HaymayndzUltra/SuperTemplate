"""
User tests for {{PROJECT_NAME}}.
"""

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import UserProfile

User = get_user_model()


class UserViewSetTestCase(APITestCase):
    """Test case for user viewset."""
    
    def setUp(self):
        # Create test users
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='AdminPass123!'
        )
        
        self.regular_user = User.objects.create_user(
            username='user1',
            email='user1@example.com',
            password='UserPass123!',
            first_name='John',
            last_name='Doe'
        )
        
        self.other_user = User.objects.create_user(
            username='user2',
            email='user2@example.com',
            password='UserPass123!'
        )
        
        # Create profiles
        UserProfile.objects.create(
            user=self.regular_user,
            job_title='Developer',
            company='Tech Corp'
        )
    
    def test_list_users(self):
        """Test listing users."""
        self.client.force_authenticate(user=self.regular_user)
        
        url = reverse('users:user-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)
    
    def test_retrieve_user(self):
        """Test retrieving a specific user."""
        self.client.force_authenticate(user=self.regular_user)
        
        url = reverse('users:user-detail', kwargs={'pk': self.regular_user.pk})
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'user1@example.com')
        self.assertIn('profile', response.data)
    
    def test_update_own_profile(self):
        """Test updating own profile."""
        self.client.force_authenticate(user=self.regular_user)
        
        url = reverse('users:user-detail', kwargs={'pk': self.regular_user.pk})
        data = {
            'first_name': 'Jane',
            'bio': 'Updated bio',
            'profile': {
                'job_title': 'Senior Developer'
            }
        }
        
        response = self.client.patch(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Jane')
        self.assertEqual(response.data['profile']['job_title'], 'Senior Developer')
    
    def test_cannot_update_other_user(self):
        """Test that users cannot update other users' profiles."""
        self.client.force_authenticate(user=self.regular_user)
        
        url = reverse('users:user-detail', kwargs={'pk': self.other_user.pk})
        data = {'first_name': 'Hacker'}
        
        response = self.client.patch(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_admin_can_update_any_user(self):
        """Test that admin can update any user."""
        self.client.force_authenticate(user=self.admin_user)
        
        url = reverse('users:user-detail', kwargs={'pk': self.regular_user.pk})
        data = {'first_name': 'Updated'}
        
        response = self.client.patch(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], 'Updated')
    
    def test_activate_user(self):
        """Test activating a user (admin only)."""
        self.regular_user.is_active = False
        self.regular_user.save()
        
        self.client.force_authenticate(user=self.admin_user)
        
        url = reverse('users:user-activate', kwargs={'pk': self.regular_user.pk})
        response = self.client.post(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.regular_user.refresh_from_db()
        self.assertTrue(self.regular_user.is_active)
    
    def test_user_search(self):
        """Test user search functionality."""
        self.client.force_authenticate(user=self.regular_user)
        
        url = reverse('users:user-search')
        response = self.client.get(url, {'q': 'john'})
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['first_name'], 'John')