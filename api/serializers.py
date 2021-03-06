from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from recipes.models import User, Recipe


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
        )


class RecipeCreateSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'description',
            'image',
            'user',
            'view_count',
            'date',
        )
        read_only_fields = ('view_count', 'date')


class RecipeReadSerializer(serializers.ModelSerializer):
    image = Base64ImageField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'description',
            'image',
            'user',
            'view_count',
            'date',
        )
        read_only_fields = ('view_count', 'date')