"""
ASGI config for Channels_websockets project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter # channels setup
from channels.auth import AuthMiddlewareStack # channels setup
import chatapp.routing # channels setup


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Channels_websockets.settings')

# application = get_asgi_application()
# channels setup
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            chatapp.routing.websocket_urlpatters
        )
    )
})
