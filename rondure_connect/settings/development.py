from .base import *
from decouple import config

# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
SITE_ID = 2
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # Use SMTP backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # Use SMTP backend


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
CORS_ALLOW_ALL_ORIGINS = True
DEBUG = True
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
