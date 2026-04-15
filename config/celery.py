"""
Celery configuration for Lucy project.

This module configures Celery with Redis as the message broker and result backend.
It sets up task routing for different queues and configures proper task acknowledgment.
"""

import os

from celery import Celery

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

app = Celery("lucy")

# Load configuration from Django settings with CELERY_ namespace
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs
app.autodiscover_tasks()

# Task routing configuration
app.conf.task_routes = {
    "apps.messages.tasks.send_*": {"queue": "outbound"},
    "apps.messages.tasks.process_incoming_*": {"queue": "inbound"},
    "apps.webhooks.tasks.*": {"queue": "webhooks"},
}

# Task execution settings
app.conf.task_acks_late = True
app.conf.task_reject_on_worker_lost = True
app.conf.worker_prefetch_multiplier = 1

# Time limits (in seconds)
app.conf.task_time_limit = 300  # 5 minutes hard limit
app.conf.task_soft_time_limit = 240  # 4 minutes soft limit

# Result backend settings
app.conf.result_expires = 3600  # Results expire after 1 hour

# Serialization
app.conf.task_serializer = "json"
app.conf.result_serializer = "json"
app.conf.accept_content = ["json"]
app.conf.timezone = "UTC"
app.conf.enable_utc = True


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Debug task for testing Celery configuration."""
    print(f"Request: {self.request!r}")
