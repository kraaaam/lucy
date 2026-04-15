"""
Production settings for Lucy project.

This module contains settings specific to the production environment.
"""

from .base import *  # noqa: F403

# Security settings
DEBUG = False

# SECURITY WARNING: update this with your production domain
ALLOWED_HOSTS = env("ALLOWED_HOSTS")  # noqa: F405

# HTTPS and security settings
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

# Production database with connection pooling
DATABASES["default"]["CONN_MAX_AGE"] = 600  # noqa: F405
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # noqa: F405

# Email backend for production
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST", default="smtp.gmail.com")  # noqa: F405
EMAIL_PORT = env.int("EMAIL_PORT", default=587)  # noqa: F405
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)  # noqa: F405
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")  # noqa: F405
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")  # noqa: F405
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="noreply@lucy.example.com")  # noqa: F405

# Production logging - JSON format for log aggregation
LOGGING["formatters"]["json_formatter"] = {  # noqa: F405
    "()": structlog.stdlib.ProcessorFormatter,  # noqa: F405
    "processor": structlog.processors.JSONRenderer(),  # noqa: F405
}

LOGGING["handlers"]["console"]["formatter"] = "json_formatter"  # noqa: F405

# Static files - configure for production CDN/S3 if needed
# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Cache settings - increase timeout for production
CACHES["default"]["TIMEOUT"] = 600  # noqa: F405

# Celery production settings
CELERY_TASK_ALWAYS_EAGER = False
CELERY_TASK_EAGER_PROPAGATES = False
