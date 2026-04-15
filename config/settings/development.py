"""
Development settings for Lucy project.

This module contains settings specific to the development environment.
"""

from .base import *  # noqa: F403

# Debug toolbar and development-specific apps
INSTALLED_APPS += [  # noqa: F405
    # Add development-specific apps here
]

# Development-specific middleware
MIDDLEWARE += [  # noqa: F405
    # Add development-specific middleware here
]

# Allow all hosts in development
if DEBUG:  # noqa: F405
    ALLOWED_HOSTS = ["*"]

# Development-specific CORS settings
CORS_ALLOW_ALL_ORIGINS = True

# Email backend for development (console)
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Enable browsable API in development
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] += [  # noqa: F405
    "rest_framework.renderers.BrowsableAPIRenderer",
]

# Disable HTTPS redirects in development
SECURE_SSL_REDIRECT = False

# Development logging - more verbose
LOGGING["loggers"]["apps"] = {  # noqa: F405
    "handlers": ["console"],
    "level": "DEBUG",
    "propagate": False,
}
