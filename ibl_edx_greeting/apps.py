"""
ibl_edx_greeting Django application initialization.
"""
import logging
from django.apps import AppConfig

logger = logging.getLogger(__name__)


class IblEdxGreetingConfig(AppConfig):
    """
    Configuration for the ibl_edx_greeting Django application.
    """

    name = "ibl_edx_greeting"
    verbose_name = "Open edX Greeting Plugin"

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "ibl_edx_greeting",
                "regex": "^api/",
                "relative_path": "urls",
            },
        }
    }
