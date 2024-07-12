from django.db import models

# Create your models here.
class strategiesList(models.Model):
    name = models.TextField(max_length=100)
    script = models.TextField(max_length=1000)
