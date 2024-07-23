from typing import Optional

from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for Product model.
    """
    category = serializers.SerializerMethodField()
    subcategory = serializers.SerializerMethodField()
    image_list = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields: tuple = ('id', 'name', 'slug', 'category', 'subcategory', 'price', 'image_list')

    @staticmethod
    def get_category(product) -> Optional[str]:
        """
        Get the category of the product.
        :param product: product object
        :return: name of the category if exists, else None
        """
        if product.subcategory and product.subcategory.category:
            return product.subcategory.category.name
        return None

    @staticmethod
    def get_subcategory(product) -> Optional[str]:
        """
        Get the sub category of the product.
        :param product: product object
        :return: name of the subcategory if exists, else None
        """
        if product.subcategory:
            return product.subcategory.name
        return None

    @staticmethod
    def get_image_list(product) -> list:
        """
        Get the image list of the product.
        :param product: product object
        :return: list of images
        """
        large = str(product.image_l).split('/')
        medium = str(product.image_m).split('/')
        small = str(product.image_s).split('/')
        return [large[2], medium[2], small[2]]
