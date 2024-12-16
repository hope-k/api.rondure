from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import RegisterView, LoginView
from .serializers import CustomRegisterSerializer


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    # The redirect URI you set on Google - https://127.0.0.1:8000/accounts/google/login/callback/
    callback_url = "https://127.0.0.1:8000/api/v1/auth/accounts/google/login/callback/"
    client_class = OAuth2Client

    def get_response(self):
        response = super().get_response()
        user = self.user

        # Determine if the user is new (example: check if `phone` or other fields are incomplete)
        is_new_user = not user.phone_number
        response.data["is_new_user"] = is_new_user

        return response


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    callback_url = "https://localhost:8000/api/v1/auth/facebook/callback/"

    # Optionally override get_response to detect new accounts:
    def get_response(self):
        response = super().get_response()
        user = self.user

        is_new_user = not user.phone_number
        response.data["is_new_user"] = is_new_user
        return response
