"""
ASGI config for rondure_connect project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from decouple import config
environment = config("ENVIRONMENT", default="production")  # Default to production

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"rondure_connect.settings.{environment}"
)

application = get_asgi_application()
