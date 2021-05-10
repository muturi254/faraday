from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from apps.utils.models import Timestamps
# Create your models here.
class Lecture(Timestamps, models.Model):
    title = models.CharField(max_length=100)
    lecturer_name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()
    duration = models.IntegerField(validators=[
        MinValueValidator(1), MaxValueValidator(10)
    ], help_text='Enter n.o of hours')
    slides_url = models.CharField(max_length=255)
    date = models.DateTimeField()
    is_required = models.BooleanField(default=True)

    def __str__(self):
        return self.title