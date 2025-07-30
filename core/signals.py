from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added
from .models import User
import logging

logger = logging.getLogger(__name__)

@receiver(social_account_added)
def store_user(request, sociallogin, **kwargs):
    data = sociallogin.account.extra_data

    name = data.get("name")
    email = data.get("email")
    profile = data.get("picture")
    google_id = data.get("id")

    # Check if user already exists, if not save in custom table
    if not email:
        logger.warning("Missing email")
        return 

    if not User.objects.filter(email=email).exists():
        User.objects.create(
            name=name,
            email=email,
            profile_pic=profile,
            google_id=google_id
        )

        logger.info(f"Stored new social login user: {email}")
