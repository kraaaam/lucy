import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class User(BaseModel, AbstractUser):
    pass


class Message(BaseModel):
    TELEGRAM = "telegram"
    MESSENGER = "messenger"
    VIBER = "viber"
    SMS = "sms"
    EMAIL = "email"

    SERVICE_CHOICES = (
        (TELEGRAM, "Telegram"),
        (MESSENGER, "Messenger"),
        (VIBER, "Viber"),
        (SMS, "SMS"),
        (EMAIL, "Email"),
    )

    sender = models.CharField(max_length=255, blank=True, null=True)
    receiver = models.CharField(max_length=255, blank=True, null=True)
    service = models.CharField(
        max_length=50, choices=SERVICE_CHOICES, blank=True, null=True
    )
    message = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(default=False)
