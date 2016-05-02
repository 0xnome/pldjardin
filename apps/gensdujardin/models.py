import os

from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.text import slugify


def content_file_name(instance, filename):
    return os.path.join(*['avatars', str(instance.user.pk)+"_"+slugify(instance.user.username), filename])

class  Profil(models.Model):
    user = models.OneToOneField(User)
    ville = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to=content_file_name, blank=True, null=True)
    presentation = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = Profil.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)