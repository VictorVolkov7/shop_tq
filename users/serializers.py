from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user model.
    """

    class Meta:
        model = User
        fields: tuple = ('email', 'password', 'first_name', 'last_name')

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        """
        Create a new User.
        """
        password: str = validated_data.pop('password', None)
        instance = User.objects.create(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
