from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


def content_file_name(instance, filename):
    return '/'.join(['avatars', instance.user.username, filename])


class  Utilisateur(models.Model):
    user = models.OneToOneField(User)
    ville = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to=content_file_name, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = Utilisateur.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)