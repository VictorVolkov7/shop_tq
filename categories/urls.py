from django.urls import path

from categories.api_views import CategoryListAPIView
from categories.apps import CategoriesConfig

app_name = CategoriesConfig.name

urlpatterns = [
    # category routes
    path('categories/', CategoryListAPIView.as_view(), name='categories_list'),
]
