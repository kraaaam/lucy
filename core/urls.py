from django.urls import path

from .views import SendMessageAPIView

urlpatterns = [
    path("message/send/", SendMessageAPIView.as_view()),
]
