"""
URLs for ibl_edx_greeting.
"""
from django.urls import include, path
from rest_framework import routers
from ibl_edx_greeting.views import GreetingViewSet

router = routers.DefaultRouter()
router.register(r"greeting", GreetingViewSet)

urlpatterns = [
    path("v1/", include(router.urls)),
]
