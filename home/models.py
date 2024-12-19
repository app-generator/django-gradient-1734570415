# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    avatar = models.CharField(max_length=255, null=True, blank=True)
    auth_provider = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Conversation(models.Model):

    #__Conversation_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(UserTrash, on_delete=models.CASCADE)
    input_test = models.TextField(max_length=255, null=True, blank=True)
    translated_text = models.TextField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Conversation_FIELDS__END

    class Meta:
        verbose_name        = _("Conversation")
        verbose_name_plural = _("Conversation")


class Usertrash(models.Model):

    #__Usertrash_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Usertrash_FIELDS__END

    class Meta:
        verbose_name        = _("Usertrash")
        verbose_name_plural = _("Usertrash")


class Usageanalytics(models.Model):

    #__Usageanalytics_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(UserTrash, on_delete=models.CASCADE)
    chats_used = models.IntegerField(null=True, blank=True)
    last_used_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Usageanalytics_FIELDS__END

    class Meta:
        verbose_name        = _("Usageanalytics")
        verbose_name_plural = _("Usageanalytics")



#__MODELS__END
