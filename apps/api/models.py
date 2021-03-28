from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Todo_list_model(models.Model):
    name = models.CharField(max_length=100, default="")
    date = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    done = models.BooleanField(default=False)
    is_habit = models.BooleanField(default=False)
    frequency = models.IntegerField(default=None, null=True)
    is_special = models.BooleanField(default=False, null=True)
    is_daily_challenge = models.BooleanField(default=False, null=True)
    category = models.CharField(max_length=50, default="", null=True)
    points = models.IntegerField(default=0)

    foreign_key = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None)
