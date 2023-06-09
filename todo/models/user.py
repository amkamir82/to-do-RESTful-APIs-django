from django.contrib.auth.models import AbstractUser
from django.db import models as django_models

ROLE = (("1", "MANAGER"), ("2", "DEVELOPER"),)


class User(AbstractUser):
    role = django_models.CharField(choices=ROLE, max_length=16)
