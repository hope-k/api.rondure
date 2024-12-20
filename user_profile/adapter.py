from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.sites.models import Site
from allauth.core.exceptions import ImmediateHttpResponse
from django.http import JsonResponse
from allauth.account.models import EmailAddress
from rest_framework.exceptions import ValidationError


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        current_site = Site.objects.get_current()
        print("CURRENT SITE: ", current_site)

        # Set your frontend URL here
        return f"{current_site}/auth/verify-email/?confirm-email-token={emailconfirmation.key}"

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.phone_number = data.get("phone_number")
        # Save the user if commit is True
        if commit:
            user.save()
        return user


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):

        # Get the email from the social login
        email = sociallogin.account.extra_data.get("email")

        if email:
            try:
                # Check if the email exists in the database
                existing_email = EmailAddress.objects.get(email=email)

                if existing_email.user:
                    # Check if the email is already linked to a social account
                    if not existing_email.user.socialaccount_set.filter(
                        provider=sociallogin.account.provider
                    ).exists():

                        raise ValidationError(
                            detail=(
                                "An account already exists with this email address but is not linked to this social account. "
                                "Please sign in using your email and password"
                            )
                        )
            except EmailAddress.DoesNotExist:
                # If no existing email is found, allow signup
                pass
