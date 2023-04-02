from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from mainApp import views

router = routers.DefaultRouter()
router.register(r"pokemon", views.PokemonViewSet)
router.register(r"teams", views.TeamViewSet)
router.register(r"moves", views.MoveViewSet)
router.register(r"users", views.CustomUserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
