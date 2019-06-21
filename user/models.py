from django.db import models
from django.contrib.auth.models import User

ACCOUNT_TYPES = [
    ('admin', 'Admin'),
    ('superadmin', 'Superadmin')
]


class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name='useraccount', on_delete=models.CASCADE)
    type = models.CharField(choices=ACCOUNT_TYPES, null=True, blank=True, max_length=255)
