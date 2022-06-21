from django.db import models

from accounts.models import User
from orders.models import Order


class Board(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # text, order, image
    type = models.CharField(max_length=10)
    content = models.TextField()
