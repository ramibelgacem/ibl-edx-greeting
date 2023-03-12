"""
Database models for ibl_edx_greeting.
"""
from django.db import models

from model_utils.models import TimeStampedModel


class Greeting(TimeStampedModel):
    """
    TODO: replace with a brief description of the model.

    TODO: Add either a negative or a positive PII annotation to the end of this docstring.  For more
    information, see OEP-30:
    https://open-edx-proposals.readthedocs.io/en/latest/oep-0030-arch-pii-markup-and-auditing.html
    """

    message = models.CharField(max_length=255)

    def __str__(self):
        """
        Get a string representation of this model instance.
        """
        return "{}".format(self.message)
