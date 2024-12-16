"""
WSGI config for rondure_connect project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from decouple import config

from django.core.wsgi import get_wsgi_application

environment = config("ENVIRONMENT", default="production")  # Default to production

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", f"rondure_connect.settings.{environment}"
)

application = get_wsgi_application()
app = application
