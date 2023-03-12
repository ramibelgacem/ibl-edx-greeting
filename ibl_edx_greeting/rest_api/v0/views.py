"""
API Views
"""

import logging

from django.apps import apps
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from edx_rest_api_client.client import OAuthAPIClient

from ibl_edx_greeting.rest_api.v0.serializers import GreetingSerializer

logger = logging.getLogger(__name__)


class GreetingAPIView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    authentication_classes = (JwtAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    trigger_message = "hello"
    callback_message = "goodbye"
    app_config = apps.get_app_config("ibl_edx_greeting")

    def post(self, request, format=None):
        serializer = GreetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Create new greeting message: {request.data.get('message')}")

            if request.data.get("message") == GreetingAPIView.trigger_message:
                self._greeting_callback()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _greeting_callback(self):
        client = OAuthAPIClient(
            GreetingAPIView.app_config.backend_service_edx_oauth2_provider_url,
            GreetingAPIView.app_config.backend_service_edx_oauth2_key,
            GreetingAPIView.app_config.backend_service_edx_oauth2_secret,
        )
        callback_response = client.post(
            "http://local.overhang.io/ibledxgreeting/api/v0/greeting/",
            data={"message": GreetingAPIView.callback_message},
            timeout=(5, 5),
        )
        callback_response.raise_for_status()
