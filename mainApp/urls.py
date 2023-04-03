from rest_framework import routers
from mainApp import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"pokemon", views.PokemonViewSet)
router.register(r"teams", views.TeamViewSet)
router.register(r"moves", views.MoveViewSet)

urlpatterns = [path("", include(router.urls))]
