# chat/routing.py
from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/channel/<str:room_code>/', consumers.ChatConsumer, name='channel_join'),
]   