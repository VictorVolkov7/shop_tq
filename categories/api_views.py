from rest_framework import generics
from rest_framework.permissions import AllowAny

from categories.models import Category
from categories.paginators import CategoryPaginator
from categories.serializers.category import CategorySerializer


class CategoryListAPIView(generics.ListAPIView):
    """
    API endpoint to view a list of categories.
    """
    queryset = Category.objects.all().order_by('pk')
    serializer_class = CategorySerializer
    pagination_class = CategoryPaginator
    permission_classes = [AllowAny]
