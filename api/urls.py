from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RecipeViewSet, UserViewSet

app_name = 'api'

router = DefaultRouter()
router.register('recipes', RecipeViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]

