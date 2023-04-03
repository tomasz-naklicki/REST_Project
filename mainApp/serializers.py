from .models import Pokemon, Team, Move
from rest_framework import serializers


class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = [
            "name",
            "nickname",
            "type1",
            "type2",
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
        fields = ["name", "owner"]


class MoveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Move
        fields = ["name", "description", "type"]
