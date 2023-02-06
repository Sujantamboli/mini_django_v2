"""
NOTE
everytime we create/change models, we have to run to commands
1. python manage.py makemigrations
2. python manage.py migrate
"""

from django.db import models
from django.utils import timezone
from enum import Enum
# Create your models here.

# class MyChoices(Enum):
#     CHOICE1 = "developer"
#     CHOICE2 = "tester"
#     CHOICE3 = "manager"
#
#     @classmethod
#     def choices(cls):


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date= models.DateTimeField(default=timezone.now)
    published_date= models.DateTimeField(blank=True, null=True)
    another_field = models.CharField(
        max_length=250,
        choices=[("profile", "tester"), ("profile2", "developer")],
        default="DEFAULT"
    )


class Randomtable(models.Model):
    user_name = models.CharField(max_length=250)
    question = models.CharField(max_length=250)
    answer = models.TextField()
