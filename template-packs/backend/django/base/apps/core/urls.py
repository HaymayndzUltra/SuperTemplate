"""
Core URLs for {{PROJECT_NAME}}.
"""

from django.urls import path

from .views import InfoView, StatsView

app_name = 'core'

urlpatterns = [
    path('', InfoView.as_view(), name='info'),
    path('stats/', StatsView.as_view(), name='stats'),
]