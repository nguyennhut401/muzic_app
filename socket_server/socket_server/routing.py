from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from socket_server.broadcast_channel.routing import websocket_urlpatterns as socket_urls

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            socket_urls
        )
    ),
})