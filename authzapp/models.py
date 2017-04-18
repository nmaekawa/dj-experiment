from datetime import datetime
from datetime import timedelta

from django.db import models
from django.db.models.signals import post_save

from django.contrib.auth.models import User
from django.dispatch import receiver


class Profile(models.Model):
    created = models.DateTimeField(default=datetime.utcnow)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prime_consumer = models.OneToOneField(
            'Consumer',
            related_name='prime_profile',
            null=True,
            on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


def expire_in_weeks(ttl=24):
    return datetime.utcnow() + timedelta(weeks=ttl)


class Consumer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    api_key = models.CharField(max_length=50, primary_key=True)
    secret_key = models.CharField(max_length=50, blank=False, null=False)
    expire_on = models.DateTimeField(default=expire_in_weeks)
    profile = models.ForeignKey(
            'Profile',
            related_name='consumers',
            on_delete=models.CASCADE)
    #prime_profile = models.OneToOneField(
    #        Profile,
    #        parent_link=True,
    #        related_name='prime_consumer',
    #        on_delete=models.CASCADE)


