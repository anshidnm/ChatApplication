from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
from main import routing as app_routing
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            app_routing.websocket_urlpatterns
        )
    )
})