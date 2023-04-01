from django.db.models import TextChoices
from django.utils.translation import gettext_lazy


class UserTypes(TextChoices):
    USER = "U", gettext_lazy("User")
    SUPERUSER = "SU", gettext_lazy("Superuser")
