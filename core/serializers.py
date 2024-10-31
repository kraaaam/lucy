from rest_framework import serializers

from .models import Message


class SendMessageSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(required=True)
    receiver = serializers.CharField(required=True)
    service = serializers.CharField(required=True)
    message = serializers.CharField(required=True)

    class Meta:
        model = Message
        fields = [
            "sender",
            "receiver",
            "service",
            "message",
        ]
