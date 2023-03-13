"""
ibl_edx_greeting Django application initialization.
"""
from django.apps import AppConfig
from django.conf import settings


class IblEdxGreetingConfig(AppConfig):
    """
    Configuration for the ibl_edx_greeting Django application.....
    """

    name = "ibl_edx_greeting"
    verbose_name = "Open edX Greeting Plugin"
    oauth2_provider_url = "http://local.overhang.io/oauth2/access_token/"

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "ibl_edx_greeting",
                "regex": "^ibledxgreeting/",
                "relative_path": "urls",
            },
        },
    }
