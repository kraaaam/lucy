"""
Messages app configuration.
"""

from django.apps import AppConfig


class MessagesConfig(AppConfig):
    """Configuration for the messages app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.messages"
    label = "lucy_messages"
    verbose_name = "Messages"
