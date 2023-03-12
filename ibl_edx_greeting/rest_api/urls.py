"""
IBL IDX GREETING API URLs.
"""

from django.urls import include, path

urlpatterns = [
    path("v0/", include("ibl_edx_greeting.rest_api.v0.urls")),
]
