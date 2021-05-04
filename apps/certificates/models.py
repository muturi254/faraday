from django.db import models

from apps.utils.models import Timestamps
# Create your models here.
class Certificate(models.Model, Timestamps):
    name = models.CharField(max_length=100)
    description = models.TextField(Max_length=200)