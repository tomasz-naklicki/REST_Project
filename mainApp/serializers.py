from .models import Pokemon, Team, Move
from user.models import CustomUser
from user.serializers import CustomUserSerializer
from rest_framework import serializers, request
import jwt
from django.conf import settings


class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = [
            "id",
            "name",
            "nickname",
            "type1",
            "type2",
            "hp",
            "atk",
            "spatk",
            "defense",
            "spdef",
            "spd",
            "team",
            "moves",
        ]


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "owner_id"]


class MoveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Move
        fields = ["id", "name", "description", "category", "type", "power", "accuracy"]
