"""
Core models for Lucy project.

This module contains abstract base models that provide common functionality
for other models throughout the application.
"""

import uuid

from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides timestamp fields.

    Attributes:
        created_at: Timestamp when the record was created
        modified_at: Timestamp when the record was last modified
    """

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class UUIDModel(models.Model):
    """
    Abstract base model that provides a UUID field.

    Attributes:
        uid: Unique identifier for the record (UUID4)
    """

    uid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
        db_index=True,
        help_text="Unique identifier for this record",
    )

    class Meta:
        abstract = True
