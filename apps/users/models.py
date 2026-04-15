"""
User models for Lucy project.

This module contains user-related models for authentication and authorization.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.models import TimeStampedModel, UUIDModel


class User(AbstractUser, UUIDModel, TimeStampedModel):
    """
    Custom user model extending Django's AbstractUser.

    This model represents system users who can create and manage applications.
    """

    email = models.EmailField(unique=True, help_text="User's email address")

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]

    def __str__(self):
        return self.email
