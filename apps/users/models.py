"""
User models for Lucy project.

This module contains user-related models for authentication and authorization.
"""

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.core.models import TimeStampedModel, UUIDModel


class UserManager(BaseUserManager):
    """
    Custom manager for User model.

    This manager can be extended to include custom query methods for user management.
    """

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given email and password.

        Args:
            email (str): The user's email address.
            password (str, optional): The user's password. Defaults to None.
            **extra_fields: Additional fields for the user.

        Returns:
            User: The created user instance.
        """
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a superuser with the given email and password.

        Args:
            email (str): The superuser's email address.
            password (str, optional): The superuser's password. Defaults to None.
            **extra_fields: Additional fields for the superuser.

        Returns:
            User: The created superuser instance.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_verified", True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser, UUIDModel, TimeStampedModel):
    """
    Custom user model extending Django's AbstractUser.

    This model represents system users who can create and manage applications.
    """

    username = None  # Remove the username field from AbstractUser
    email = models.EmailField(unique=True, help_text="User's email address")
    is_verified = models.BooleanField(
        default=False,
        help_text="Designates whether this user has verified their email address.",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()
    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-created_at"]

    def __str__(self):
        return self.email
