from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLResolver
import chat.routing

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLResolver(
            chat.routing.websocket_urlpatterns
        )
    )
})