"""
URLs for ibl_edx_greeting.
"""

from django.urls import include, path
from rest_framework import routers


urlpatterns = [
    path('api/', include('ibl_edx_greeting.rest_api.urls')),
]
