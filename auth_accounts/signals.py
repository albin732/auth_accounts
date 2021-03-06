from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserDetailModel


@receiver(post_save, sender=User)
def create_userdetail(sender, instance, created, **kwargs):
    if created:
        UserDetailModel.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_userdetail(sender, instance, **kwargs):
    instance.userdetail.save()
