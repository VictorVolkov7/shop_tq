from rest_framework import serializers

from categories.models import Category
from categories.serializers.sub_category import SubCategorySerializer


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for category model.
    """
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields: tuple = ('pk', 'name', 'slug', 'image', 'subcategories',)
