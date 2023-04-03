from rest_framework import views, permissions, response, exceptions
from .serializers import CustomUserSerializer
from .authentication import CustomUserAuthentication
from . import utils


class RegisterAPI(views.APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        serializer.instance = utils.create_user(user_dc=data)
        return response.Response(data=serializer.data)


class LoginAPI(views.APIView):
    def post(self, request):
        username = request.data["username"]
        password = request.data["password"]

        user = utils.find_username(username=username)

        if user is None:
            raise exceptions.AuthenticationFailed("Invalid login info")
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid login info")

        token = utils.create_token(user_id=user.id)

        res = response.Response()
        res.set_cookie(key="jwt", value=token, httponly=True)
        return res


class UserAPI(views.APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = CustomUserSerializer(user)

        return response.Response(serializer.data)


class LogoutAPI(views.APIView):
    authentication_classes = (CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        res = response.Response()
        res.delete_cookie("jwt")
        res.data = {"status": "Successful logout"}
        return res
