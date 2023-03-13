"""
API Views
"""

import logging

from django.conf import settings
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication

from edx_rest_api_client.client import OAuthAPIClient
from oauth2_provider.models import Application

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

    def post(self, request):
        serializer = GreetingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Create new greeting message: {request.data.get('message')}")

            if request.data.get("message") == GreetingAPIView.trigger_message:
                self._greeting_callback()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _greeting_callback(self):
        try:
            oauth_application = Application.objects.filter(
                authorization_grant_type=Application.GRANT_CLIENT_CREDENTIALS
            )[0]
        except IndexError:
            logger.warning("No Oauth2 application founds with client credentials grant")
            return

        client = OAuthAPIClient(
            f"{settings.LMS_ROOT_URL}/oauth2/access_token/",  # it could be defined in the IblEdxGreetingConfig class but it does not work # noqa: E501
            oauth_application.client_id,
            oauth_application.client_secret,
        )
        callback_response = client.post(
            f"{settings.LMS_ROOT_URL}/ibledxgreeting/api/v0/greeting/",
            data={"message": GreetingAPIView.callback_message},
            timeout=(5, 5),
        )
        callback_response.raise_for_status()
