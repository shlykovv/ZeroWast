from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_business = models.BooleanField(default=False, verbose_name="Бизнес-пользователь")

    def __str__(self):
        return self.username
