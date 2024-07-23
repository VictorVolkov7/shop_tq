from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Create a new user controller.
    """
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
