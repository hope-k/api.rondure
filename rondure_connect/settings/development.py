from .base import *
from decouple import config

# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
SITE_ID = 2
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # Use SMTP backend
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # Use SMTP backend
EMAIL_HOST = config("EMAIL_HOST", default="")  # Example: Use Gmail's SMTP server
EMAIL_PORT = config("EMAIL_PORT", default=587)  # Port for TLS
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=False, cast=bool)  # Enable TLS
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")  # Your SMTP email
EMAIL_HOST_PASSWORD = config(
    "EMAIL_HOST_PASSWORD", default=""
)  # Your email password or app password
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="")  #


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
