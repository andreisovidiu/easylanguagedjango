from django.db import models

class Strategy(models.Model):
    strategy = models.TextField(max_length=1000)
    