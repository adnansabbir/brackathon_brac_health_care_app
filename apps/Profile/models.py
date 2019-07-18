from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    GENDER_CHOICE = (
        ('m', "MALE"),
        ('f', "FEMALE"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=255, null=True, blank=False, verbose_name="Phone Number")
    nid = models.CharField(max_length=40, null=True, blank=False, verbose_name="NID Number")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True, blank=False)
    birth_date = models.DateField(null=True, blank=False)

    # name is from user model
    # BRAC registration number is the username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
