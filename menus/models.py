from django.db import models

from accounts.models import User
from orders.models import Order


class Menu(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu = models.JSONField(default=dict)

    def price(self):
        return sum(self.menu.values())
