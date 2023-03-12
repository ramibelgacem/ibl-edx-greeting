"""
URLs for ibl_edx_greeting.
"""

from django.urls import include, path


urlpatterns = [
    path("api/", include("ibl_edx_greeting.rest_api.urls")),
]
