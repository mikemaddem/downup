from django.db import models
from user.models import UserProfile


class HTTPGetTracker(models.Model):
    url = models.URLField(blank=True, null=True)
    creator = models.ForeignKey(UserProfile, related_name='getcreator', on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class PINGTracker(models.Model):
    ip = models.CharField(default='0.0.0.0', max_length=255)
    port = models.PositiveIntegerField(default=80)
    creator = models.ForeignKey(UserProfile, related_name='pingcreator', on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)