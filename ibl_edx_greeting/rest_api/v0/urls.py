"""
IBL IDX GREETING API V0 URLs.
"""

from django.urls import include, path
from rest_framework import routers

from ibl_edx_greeting.rest_api.v0.views import GreetingAPIView


urlpatterns = [
    path('greeting/', GreetingAPIView.as_view(), name='greeting'),
]
