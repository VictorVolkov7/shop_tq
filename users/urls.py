from django.urls import path

from users.api_views import TokenObtainPairView, TokenRefreshView, UserCreateAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # users routes
    path('register/', UserCreateAPIView.as_view(), name='categories_list'),

    # simple-jwt routes
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
