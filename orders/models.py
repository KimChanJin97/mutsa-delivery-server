from django.db import models

from accounts.models import User


class Order(models.Model):
    leader = models.ForeignKey(User, related_name='order_lead_user', on_delete=models.CASCADE)
    brand = models.CharField(max_length=40)
    time = models.DateTimeField()
    joined_user = models.ManyToManyField(User, related_name='order_joined_user')

    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)

    def joined_user_length(self):
        return self.joined_user.count()
