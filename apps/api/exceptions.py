"""
Custom exception handlers for the API.

This module provides custom exception handling for consistent API error responses.
"""

import structlog
from rest_framework.views import exception_handler

logger = structlog.get_logger(__name__)


def custom_exception_handler(exc, context):
    """
    Custom exception handler for DRF.

    This handler ensures all exceptions are logged and returned with a consistent format.

    Args:
        exc: The exception that was raised
        context: Context information about the exception

    Returns:
        Response: DRF Response object with error details
    """
    # Call DRF's default exception handler first
    response = exception_handler(exc, context)

    if response is not None:
        # Log the exception
        logger.error(
            "api_exception",
            exception=str(exc),
            status_code=response.status_code,
            path=context.get("request").path if context.get("request") else None,
        )

        # Customize the response format
        custom_response_data = {"errors": response.data, "status_code": response.status_code}
        response.data = custom_response_data

    return response
