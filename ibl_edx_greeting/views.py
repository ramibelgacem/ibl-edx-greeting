from rest_framework import viewsets
from rest_framework import permissions

from ibl_edx_greeting.models import Greeting
from ibl_edx_greeting.serializers import GreetingSerializer


class GreetingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Greeting.objects.all()
    serializer_class = GreetingSerializer
    permission_classes = [permissions.IsAuthenticated]
