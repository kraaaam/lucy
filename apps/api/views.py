"""
API views for Lucy project.

This module contains shared API views and utilities.
"""

from datetime import datetime

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheckView(APIView):
    """
    Health check endpoint for monitoring and load balancing.

    Returns a simple JSON response indicating the service is healthy.
    """

    permission_classes = [AllowAny]

    def get(self, request):
        """
        Handle GET request for health check.

        Returns:
            Response: JSON response with status and timestamp
        """
        return Response(
            {"status": "healthy", "timestamp": datetime.utcnow().isoformat()},
            status=status.HTTP_200_OK,
        )
