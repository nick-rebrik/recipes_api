from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from recipes.models import User, Recipe


class RecipeSerializer(serializers.ModelSerializer):
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
        )
        read_only_fields = ('view_count',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
        )
