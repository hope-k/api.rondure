from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError as DjangoValidationError
from allauth.account.models import EmailAddress


try:
    from allauth.account import app_settings as allauth_account_settings
    from allauth.account.adapter import get_adapter
    from allauth.account.utils import setup_user_email
    from allauth.socialaccount.models import EmailAddress
except ImportError:
    raise ImportError("allauth needs to be added to INSTALLED_APPS.")


class CustomUserDetailsSerializer(UserDetailsSerializer):
    phone_number = serializers.CharField()
    is_email_verified = serializers.SerializerMethodField()

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            "phone_number",
            "is_email_verified",
        )

    def get_is_email_verified(self, obj):
        # Check if the user's email is verified
        email_address = EmailAddress.objects.filter(user=obj, email=obj.email).first()
        return email_address.verified if email_address else False


class CustomRegisterSerializer(RegisterSerializer):
    username = None
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)

    def validate_email(self, email):
        User = get_user_model()
        email = get_adapter().clean_email(email)
        if allauth_account_settings.UNIQUE_EMAIL:
            if email and EmailAddress.objects.is_verified(email):
                raise serializers.ValidationError(
                    _(
                        "This email is already associated with an account that is verified."
                    ),
                )
            if User.objects.filter(email=email).exists():
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address.")
                )

        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def save(self, request):
        return super().save(request)

    def validate(self, data):
        return super().validate(data)

    def get_cleaned_data(self):
        return {
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "phone_number": self.validated_data.get("phone_number", ""),
        }
