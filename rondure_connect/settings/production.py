from .base import *


SITE_ID = 1

ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="", cast=Csv())
DEBUG = config("DEBUG", default=False, cast=bool)

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"  # Use SMTP backend
EMAIL_HOST = config("EMAIL_HOST", default="")  # Example: Use Gmail's SMTP server
EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)  # Port for TLS
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=False, cast=bool)  # Enable TLS
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")  # Your SMTP email
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")  # Your email password or app password
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="")  #

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME", default=""),  # Replace with your databasename
        "USER": config("DB_USER", default=""),  # Replace with your PostgreSQL user
        "PASSWORD": config("DB_PASSWORD", default=""),  # Replace with your PostgreSQL password
        "HOST": config("DB_HOST", default=""),  # Or the hostname of your PostgreSQL server
        "PORT": config("DB_PORT", default=""),  # Default PostgreSQL port
    }
}
