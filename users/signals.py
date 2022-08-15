from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
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


@receiver(post_save, sender=Profile)
def updateUser(sender, instance, created, **kwargs):
    """
    when profile is edited, edit the User data as well
    """
    if not created:
        profile = instance
        user = profile.user

        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    """
    when profile is deleted, delete the user as well
    """
    user = instance.user
    user.delete()
