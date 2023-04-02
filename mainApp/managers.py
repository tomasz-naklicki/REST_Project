from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from .usertypes import UserTypes


class CustomUserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):
        if not username:
            raise ValueError(_("Username must be valid"))
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **kwargs):
        kwargs.setdefault("user_type", UserTypes.ADMIN)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get("user_type") is not UserTypes.ADMIN:
            raise ValueError(_("Admins must have an Admin type"))

        return self.create_user(username, password, **kwargs)
