from django.urls import include, path
from rest_framework import routers

from .views import UserViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(v1_router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
    path('users/<int:pk>/subscribe/',
         UserViewSet.as_view({'post': 'subscribe'}), name='user-subscribe'),
]
