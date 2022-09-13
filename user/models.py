from django.contrib.auth.models import AbstractUser, User
from django.db import models

from crm_project import settings


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f'{self.user}'

