from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.sites.models import Site


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        current_site = Site.objects.get_current()
        print('CURRENT SITE: ', current_site)

        # Set your frontend URL here
        return f"{current_site}/auth/verify-email/?confirm-email-token={emailconfirmation.key}"

    def save_user(self, request, user, form, commit=True):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.phone_number = data.get("phone_number")
        user.save()
        return user
