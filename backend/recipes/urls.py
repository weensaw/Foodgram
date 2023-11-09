from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes.views import (CustomIngredientViewSet,
                           CustomRecipeViewSet, TagViewSet)


v1_router = DefaultRouter()
v1_router.register(r'ingredients', CustomIngredientViewSet)
v1_router.register(r'recipes', CustomRecipeViewSet)
v1_router.register(r'tags', TagViewSet, basename='tags')


urlpatterns = [
    path('', include(v1_router.urls)),
]
