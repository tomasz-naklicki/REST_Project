from django.urls import path, include
from .views import RegisterAPI, LoginAPI, UserAPI, LogoutAPI

urlpatterns = [
    path("register/", RegisterAPI.as_view(), name="register"),
    path("login/", LoginAPI.as_view(), name="login"),
    path("account/", UserAPI.as_view(), name="account"),
    path("logout/", LogoutAPI.as_view(), name="logout"),
]
