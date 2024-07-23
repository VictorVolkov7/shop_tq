from rest_framework import serializers

from cart.models import ShoppingCart
from cart.serializers.cart_item import CartItemViewSerializer


class CartSerializer(serializers.ModelSerializer):
    """
    Serializer for cart model.
    """
    class Meta:
        model = ShoppingCart
        fields: tuple = ('user', 'items', 'total_quantity', 'total_cost',)
        read_only_fields: tuple = ('user', 'items', 'total_quantity', 'total_cost',)


class CartViewSerializer(serializers.ModelSerializer):
    """
    Serializer for cart view.
    """
    items = CartItemViewSerializer(many=True, source='cartitem_set')

    class Meta:
        model = ShoppingCart
        fields: tuple = ('user', 'items', 'total_quantity', 'total_cost',)
        read_only_fields: tuple = ('user', 'items', 'total_quantity', 'total_cost',)
