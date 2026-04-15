"""
Platforms app configuration.
"""

from django.apps import AppConfig


class PlatformsConfig(AppConfig):
    """Configuration for the platforms app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.platforms"
    verbose_name = "Platforms"
