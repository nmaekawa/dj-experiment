from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    consumer_key = models.CharField(max_length=50, blank=True)
    secret_key = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

