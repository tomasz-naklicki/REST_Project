from user.usertypes import UserTypes
from rest_framework import serializers
from .utils import CustomUserDataClass


class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    user_type = serializers.ChoiceField(
        choices=UserTypes.choices, default=UserTypes.USER
    )

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        return CustomUserDataClass(**data)
