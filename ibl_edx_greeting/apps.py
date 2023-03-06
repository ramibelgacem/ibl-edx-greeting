"""
ibl_edx_greeting Django application initialization.
"""
import logging
from django.apps import AppConfig
from edx_django_utils.plugins import PluginSettings, PluginURLs
from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType

logger = logging.getLogger(__name__)


class IblEdxGreetingConfig(AppConfig):
    """
    Configuration for the ibl_edx_greeting Django application.
    """

    name = "ibl_edx_greeting"
    label = "ibl_edx_greeting"
    verbose_name = "Open edX Greeting Plugin"

    plugin_app = {
        # Configuration setting for Plugin URLs.
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: name,
                PluginURLs.REGEX: f"^{name}/",
                PluginURLs.RELATIVE_PATH: "urls",
            }
        },
        # Configuration setting for Plugin Settings for this app.
        PluginSettings.CONFIG: {
            ProjectType.LMS: {
                SettingsType.PRODUCTION: {
                    PluginSettings.RELATIVE_PATH: "settings.production"
                },
                SettingsType.COMMON: {PluginSettings.RELATIVE_PATH: "settings.common"},
            }
        },
    }

    def ready(self):
        logger.debug("{label} is ready.".format(label=self.label))
