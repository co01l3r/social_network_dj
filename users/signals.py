from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def createProfile(sender, instance, created, **kwargs):
    """
    when user is created, generate profile based on given info
    """
    if created:
        profile = Profile.objects.create(
            user=instance,
            username=instance.username,
            email=instance.email,
            name=instance.first_name
        )
