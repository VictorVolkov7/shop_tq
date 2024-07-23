from rest_framework.pagination import PageNumberPagination


class CategoryPaginator(PageNumberPagination):
    """
    Custom paginator class for categories.
    """
    page_size: int = 5  # Number of elements per page
    page_size_query_param: str = 'page_size'  # Query parameter to specify the number of elements on the page
    max_page_size: int = 50  # Maximum number of elements per page
