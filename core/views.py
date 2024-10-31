from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SendMessageSerializer


class SendMessageAPIView(APIView):
    serializer_class = SendMessageSerializer

    def post(self, request):
        # TODO: standardize the response format
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data)
