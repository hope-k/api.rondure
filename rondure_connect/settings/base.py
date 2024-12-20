"""
Django settings for rondure_connect project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path
from decouple import config, Csv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
print(config("APP_SECRET_KEY", default="Not Found"))
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("APP_SECRET_KEY", default="DEFAULT")
# SECURITY WARNING: don't run with debug turned on in production!
"""
Set the necessary configurations for a Python Django project.
# Parameters:
# - DEBUG: Indicates whether debug mode is on (True) or off (False) in production.
# - AUTH_USER_MODEL: The user profile model used for authentication (string).
# - DRF_STANDARDIZED_ERRORS: Configuration options for standardized errors in Django Rest Framework (dictionary).
# - EMAIL_BACKEND: The email backend used for sending emails (string).
# - ALLOWED_HOSTS: A list of allowed host names for the project (list of strings).

Returns: None
None
"""
# settings.py
APPEND_SLASH = False
AUTH_USER_MODEL = "user_profile.UserProfile"
DRF_STANDARDIZED_ERRORS = {"ENABLE_IN_DEBUG_FOR_UNHANDLED_EXCEPTIONS": True}

CORS_ALLOWED_ORIGINS = ["http://localhost:3000", "https://rondure.vercel.app"]
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = ["http://localhost:3000", "https://rondure.vercel.app"]
# ----
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_ADAPTER = "user_profile.adapter.CustomAccountAdapter"
SOCIALACCOUNT_ADAPTER = "user_profile.adapter.CustomSocialAccountAdapter"

CSRF_COOKIE_HTTPONLY = True  # Ensures cookies are HttpOnly
CSRF_COOKIE_SECURE = True
# ------


# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
   
        "APP": {
            "client_id": config("GOOGLE_CLIENT_ID", default=""),
            "secret": config("GOOGLE_CLIENT_SECRET", default=""),
            "key": "",
        },
    },
    "facebook": {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        # use key 'APP' not 'APPS'
        "APP": {
            "client_id": config("FACEBOOK_CLIENT_ID", default=""),
            "secret": config("FACEBOOK_CLIENT_SECRET", default=""),
            "key": "",
        },
    },
}


USE_JWT = True
REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False,
    "USER_DETAILS_SERIALIZER": "user_profile.serializers.CustomUserDetailsSerializer",
    "REGISTER_SERIALIZER": "user_profile.serializers.CustomRegisterSerializer",
    "JWT_AUTH_RETURN_EXPIRATION": True,
}
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

# Application definition
REST_FRAMEWORK = {
    # other settings
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
}
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
]


INSTALLED_APPS = [
    # Django core apps
    "django.contrib.sites",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    # Third-party apps
    "drf_material",
    "rest_framework",
    "dj_rest_auth",
    "drf_spectacular",
    "drf_standardized_errors",
    "rest_framework.authtoken",
    "allauth",
    "allauth.account",
    "dj_rest_auth.registration",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
    # Custom apps
    "user_profile",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Add the account middleware(allauth):
    "allauth.account.middleware.AccountMiddleware",
    # whitenoise for static files
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "rondure_connect.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # `allauth` needs this from django
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "rondure_connect.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
