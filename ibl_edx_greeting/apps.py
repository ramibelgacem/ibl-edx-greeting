"""
ibl_edx_greeting Django application initialization.
"""
from django.apps import AppConfig


class IblEdxGreetingConfig(AppConfig):
    """
    Configuration for the ibl_edx_greeting Django application.....
    """

    name = "ibl_edx_greeting"
    verbose_name = "Open edX Greeting Plugin"

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "ibl_edx_greeting",
                "regex": "^ibledxgreeting/",
                "relative_path": "urls",
            },
        },
        "settings_config": {
            "lms.djangoapp": {
                "common": {"relative_path": "settings.base"},
            }
        },
    }
