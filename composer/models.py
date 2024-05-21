from django.db import models

class Strategy(models.Model):
    script = models.TextField(max_length=1000)
    