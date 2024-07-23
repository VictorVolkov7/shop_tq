from rest_framework import serializers

from categories.models import SubCategory


class SubCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the SubCategory model.
    """

    class Meta:
        model = SubCategory
        fields: tuple = ('pk', 'name', 'slug', 'image',)
