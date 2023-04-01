from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy
from .usertypes import UserTypes


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError(gettext_lazy("Username must be valid"))
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault("user_type", UserTypes.SUPERUSER)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("user_type") is not UserTypes.SUPERUSER:
            raise ValueError(gettext_lazy("Superusers must have a Superuser type"))
        return self.create_user(username, password, **kwargs)
