from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Pokemon, Team, Move, CustomUser
from .serializers import (
    PokemonSerializer,
    MoveSerializer,
    TeamSerializer,
    CustomUserSerializer,
)


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by("name")
    serializer_class = PokemonSerializer
    permission_classes = [permissions.IsAuthenticated]


class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all().order_by("name")
    serializer_class = MoveSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by("name")
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by("username")
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
