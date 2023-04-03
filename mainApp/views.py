from rest_framework import viewsets, permissions, request, exceptions
from .models import Pokemon, Team, Move
from .permissions import IsSuperownerOrReadOnly
from .serializers import (
    PokemonSerializer,
    MoveSerializer,
    TeamSerializer,
)
from django.http import HttpResponseRedirect
from user.authentication import CustomUserAuthentication
from rest_framework.response import Response


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all().order_by("name")
    serializer_class = PokemonSerializer
    permission_classes = (IsSuperownerOrReadOnly,)
    authentication_classes = (CustomUserAuthentication,)


class MoveViewSet(viewsets.ModelViewSet):
    queryset = Move.objects.all().order_by("name")
    serializer_class = MoveSerializer
    permission_classes = (IsSuperownerOrReadOnly,)
    authentication_classes = (CustomUserAuthentication,)


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by("name")
    serializer_class = TeamSerializer
    permission_classes = (IsSuperownerOrReadOnly,)
    authentication_classes = (CustomUserAuthentication,)
