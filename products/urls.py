from django.urls import path

from products.api_views import ProductListAPIView
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    # product routes
    path('products/', ProductListAPIView.as_view(), name='product-list'),
]