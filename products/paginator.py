from rest_framework.pagination import PageNumberPagination


class ProductPaginator(PageNumberPagination):
    """
    Custom paginator class for products.
    """
    page_size: int = 10  # Number of elements per page
    page_size_query_param: str = 'page_size'  # Query parameter to specify the number of elements on the page
    max_page_size: int = 50  # Maximum number of elements per page
