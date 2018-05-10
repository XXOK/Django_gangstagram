from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    link = models.URLField()
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

class User(models.Model):
    username = models.CharField(max_length=32, null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=128, null=True)