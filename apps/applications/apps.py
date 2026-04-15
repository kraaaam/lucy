"""
Applications app configuration.
"""

from django.apps import AppConfig


class ApplicationsConfig(AppConfig):
    """Configuration for the applications app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.applications"
    verbose_name = "Applications"
