from django.db import models

# Create your models here.
class strategiesList(models.Model):
    strategyName = models.TextField(max_length=100)
    strategyScript = models.TextField(max_length=1000)
