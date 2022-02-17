from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from recipes.models import User, Recipe
from .serializers import (RecipeCreateSerializer, RecipeReadSerializer,
                          UserSerializer)


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().select_related('user')
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('user', 'view_count')
    search_fields = ('title',)

    def get_serializer_class(self):
        if self.action == 'create':
            return RecipeCreateSerializer
        return RecipeReadSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.view_count += 1
        obj.save(update_fields=('view_count',))
        return super().retrieve(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
