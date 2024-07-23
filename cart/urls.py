from django.urls import path


from cart.api_views import CartAddItemAPIView, CartListAPIView, CartDeleteAPIView, CartRemoveItemAPIView
from cart.apps import CartConfig

app_name = CartConfig.name

urlpatterns = [
    # cart routes
    path('cart/add/<str:slug>/', CartAddItemAPIView.as_view(), name='add-product'),
    path('cart/remove/<str:slug>/', CartRemoveItemAPIView.as_view(), name='delete-product'),
    path('cart/', CartListAPIView.as_view(), name='cart-list'),
    path('cart/clear/', CartDeleteAPIView.as_view(), name='cart-delete'),
]
