from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

 