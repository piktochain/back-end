from django.db import models
from django.utils import timezone


class KeyImage(models.Model):
    user_uuid = models.TextField(default=None)
    key_uuid = models.TextField(default=None, unique=True)
    key_img = models.TextField(default=None)
