"""
Database models for ibl_edx_greeting.
"""
from django.db import models

from model_utils.models import TimeStampedModel


class Greeting(TimeStampedModel):
    """This model represent the greeting message"""

    message = models.CharField(max_length=255)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return "{}".format(self.message)
