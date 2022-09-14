from django.urls import re_path

from . import consumers

websocket_urlpatters = [
    re_path(r'ws/socker-server/', consumers.ChatConsumer.as_asgi())
]