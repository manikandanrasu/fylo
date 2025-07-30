from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added

from .models import User

@receiver(social_account_added)
def store_user(request, sociallogin, **kwargs):
    data = sociallogin.account.extra_data

    name = data.get("name")
    email = data.get("email")
    profile = data.get("picture")
    google_id = data.get("id")

    # Check if user already exists, if not save in custom table
    user = User.objects.filter(email=email).exists()

    if not user:
        User.objects.create(
            name=name,
            email=email,
            profile_pic=profile,
            google_id =google_id
        )
