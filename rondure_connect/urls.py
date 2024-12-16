"""
URL configuration for rondure_connect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from user_profile.views import GoogleLogin, FacebookLogin
from dj_rest_auth.registration.views import ResendEmailVerificationView, VerifyEmailView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path(
        "api/v1/",
        include(
            [
                path("admin/", admin.site.urls),
                path("auth/", include("dj_rest_auth.urls")),
                path(
                    "auth/signup/",
                    include("dj_rest_auth.registration.urls"),
                ),
                path("auth/accounts/", include("allauth.urls")),
                path("auth/google/", GoogleLogin.as_view(), name="google_login"),
                path(
                    "auth/facebook/",
                    FacebookLogin.as_view(),
                    name="facebook_login",
                ),
                path("auth/refresh-token/", TokenRefreshView.as_view()),
                path("auth/verify-email/", VerifyEmailView.as_view()),
                path(
                    "auth/resend-verification/",
                    ResendEmailVerificationView.as_view(),
                ),
            ]
        ),
    )
]
