from rest_framework import serializers

from ibl_edx_greeting.models import Greeting


class GreetingSerializer(serializers.ModelSerializer):
    """Greeting Serializer"""

    class Meta:
        model = Greeting
        fields = ["message"]
