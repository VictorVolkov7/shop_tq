from rest_framework import serializers

from cart.models import CartItem
from products.serializers import ProductSerializer


class CartItemViewSerializer(serializers.ModelSerializer):
    """
    Serializer for cart item model.
    """
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields: tuple = ('product', 'quantity',)
        read_only_fields: tuple = ('product', 'quantity')
