"""
ibl_edx_greeting Django application initialization.
"""
import logging
from django.apps import AppConfig

logger = logging.getLogger(__name__)


class IblEdxGreetingConfig(AppConfig):
    """
    Configuration for the ibl_edx_greeting Django application.....
    """

    name = "ibl_edx_greeting"
    verbose_name = "Open edX Greeting Plugin"
    backend_service_edx_oauth2_provider_url = 'http://local.overhang.io/oauth2/access_token/'
    backend_service_edx_oauth2_key = 'login-service-client-id'
    backend_service_edx_oauth2_secret = 'NeXQdDN25eduTeScjAQNLaHYOdliu1XK8ZChie9x8QATTpIphp9MYr2qS76RVl0jfs01cUXXvPGtb7hf6mTZRt3qMPMVwJoqVruGumWG2CyuFbB6nanQhgEBUnuQqNj1'

    plugin_app = {
        "url_config": {
            "lms.djangoapp": {
                "namespace": "ibl_edx_greeting",
                "regex": "^ibledxgreeting/",
                "relative_path": "urls",
            },
        },
    }
