from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class UserTypes(TextChoices):
    USER = "U", _("User")
    SUPERUSER = "SU", _("Superuser")
    ADMIN = "AD", _("Admin")
