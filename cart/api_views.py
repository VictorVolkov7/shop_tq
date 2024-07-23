from rest_framework import status
from rest_framework.generics import ListAPIView, DestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import ShoppingCart, CartItem
from cart.serializers.shopping_cart import CartSerializer, CartViewSerializer
from products.models import Product


class CartAddItemAPIView(APIView):
    """
    API endpoint that allows users to add items to their cart.
    """
    serializer_class = CartViewSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Creating products/cart or adding products to an existing cart.
        If the product exists, then the quantity increases by one.
        :return: response with user's shopping cart
        """
        slug: str = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)

        # create or get the current user's shopping cart
        cart, created = ShoppingCart.objects.get_or_create(user=request.user)

        # create or get an item in the current user's shopping cart
        cart_item, created = CartItem.objects.get_or_create(product=product, cart=cart)

        if not created:
            # Item already exists, update quantity
            cart_item.quantity += 1
            cart_item.save()

        cart.calculate_totals()

        # Serializing cart product data
        cart_data = self.serializer_class(cart).data
        return Response({'cart': cart_data}, status=status.HTTP_200_OK)


class CartRemoveItemAPIView(APIView):
    """
    API endpoint that allows user to update their cart.
    """
    serializer_class = CartViewSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        """
        Removing an existing item from the shopping cart.
        If the product quantity > 1, decreases by one.
        :return: response with user's shopping cart
        """
        slug: str = kwargs.get('slug')
        product = get_object_or_404(Product, slug=slug)

        # get the current user's shopping cart
        cart = ShoppingCart.objects.get(user=request.user)

        # get an item in the current user's shopping cart
        cart_item = get_object_or_404(CartItem, product=product, cart=cart)

        # cart items quantity check
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()

        cart.calculate_totals()

        cart_data = self.serializer_class(cart).data
        return Response({'cart': cart_data}, status=status.HTTP_200_OK)


class CartListAPIView(ListAPIView):
    """
    API endpoint for viewing the cart.
    """
    serializer_class = CartViewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ShoppingCart.objects.filter(user=self.request.user)


class CartDeleteAPIView(DestroyAPIView):
    """
    API endpoint for clearing a cart.
    """
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return ShoppingCart.objects.filter(user=self.request.user)
