import dataclasses
import jwt
import datetime
from .models import CustomUser
from django.conf import settings


@dataclasses.dataclass
class CustomUserDataClass:
    id: int = None
    username: str = ""
    password: str = None
    user_type: str = "U"

    @classmethod
    def from_instance(cls, user):
        return cls(
            id=user.id,
            username=user.username,
            password=user.password,
            user_type=user.user_type,
        )


def create_user(user_dc):
    user = CustomUser(
        username=user_dc.username,
        user_type=user_dc.user_type,
    )
    if user_dc.password is not None:
        user.set_password(user_dc.password)

    user.save()

    return CustomUserDataClass.from_instance(user)


def find_username(username):
    return CustomUser.objects.filter(username=username).first()


def create_token(user_id):
    payload = dict(
        id=user_id,
        exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow(),
    )
    return jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
