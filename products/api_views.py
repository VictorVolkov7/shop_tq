from rest_framework import generics
from rest_framework.permissions import AllowAny

from products.models import Product
from products.paginator import ProductPaginator
from products.serializers import ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    """
    API endpoint to view a list of products.
    """
    queryset = Product.objects.select_related('subcategory__category').all().order_by('pk')
    serializer_class = ProductSerializer
    pagination_class = ProductPaginator
    permission_classes = [AllowAny]
