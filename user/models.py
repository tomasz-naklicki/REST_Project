from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from .usertypes import UserTypes


# User model
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    user_type = models.CharField(
        max_length=2,
        choices=UserTypes.choices,
        default=UserTypes.USER,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.username
