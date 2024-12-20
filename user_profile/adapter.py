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
    # use this method if you want to link social acc to local acc
    def pre_social_login(self, request, sociallogin):
        pass
