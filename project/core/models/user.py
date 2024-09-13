from django.contrib.auth.models import AbstractUser
from django.db import models

from .base import BaseModel


class CustomUser(AbstractUser, BaseModel):
    username = models.EmailField("Email Address", unique=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.id)
