from django.db import models

from apps.utils.models import Timestamps
# Create your models here.
class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    lecturer_name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    slides_url = models.CharField(max_length=255)
    date = models.DateTimeField()