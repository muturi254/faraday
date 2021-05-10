from django.db import models

from apps.utils.models import Timestamps

# Create your models here.
class WaitListEntry(Timestamps, models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True
    )
    notes = models.TextField()

    class Meta:
        verbose_name_plural = 'Wait list entries'