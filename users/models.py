from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver
from .email import send_welcome_email


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    farmer_name = models.CharField(max_length=60, blank=True)
    farmer_photo = ImageField(blank=True, manual_crop="")
    farmer_bio = models.TextField(max_length=500, blank=True)
    farm_name = models.CharField(max_length=60, blank=True)
    farm_photo = ImageField(blank=True, manual_crop="")
    farm_description = models.TextField(max_length=500, blank=True)
    farm_location = models.CharField(max_length=60, blank=True)
    farm_tel = models.CharField(max_length=60,blank=True)
    farm_email = models.EmailField(max_length=255,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username



    @receiver(post_save, sender=User)
    def update_profile_signal(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
