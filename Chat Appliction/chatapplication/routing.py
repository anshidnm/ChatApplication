from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from main import routing as app_routing

application = ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(
        URLRouter(
            app_routing.websocket_urlpatterns
        )
    )
})