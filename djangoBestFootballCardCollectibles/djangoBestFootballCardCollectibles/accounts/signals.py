from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BFCCUser, Profile


@receiver(post_save, sender=BFCCUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=BFCCUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
