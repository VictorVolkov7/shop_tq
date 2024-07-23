from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView as BaseTokenObtainPairView, \
    TokenRefreshView as BaseTokenRefreshView

from users.serializers import UserSerializer


@extend_schema(
    summary="Create a new user controller."
)
class UserCreateAPIView(generics.CreateAPIView):
    """
    Create a new user controller.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


@extend_schema(
    summary="Используется для запроса пары токенов (access и refresh).",
)
class TokenObtainPairView(BaseTokenObtainPairView):
    """
    A placeholder for a class to supplement documentation.
    """
    pass


@extend_schema(
    summary="Используется для обновления access-токена при истечении его срока действия.",
)
class TokenRefreshView(BaseTokenRefreshView):
    """
    A placeholder for a class to supplement documentation.
    """
    pass
