from django.core.handlers.asgi import get_asgi_application

# Define the ASGI application
application = get_asgi_application()

# This is required for Vercel to work correctly
def handler(request, *args, **kwargs):
    return application(request, *args, **kwargs)
