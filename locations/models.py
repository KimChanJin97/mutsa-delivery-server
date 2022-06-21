from django.db import models

from accounts.models import User


class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
