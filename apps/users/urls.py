from django.urls import path, include
from rest_framework import routers

from .viewsets import UserViewSet

app_name = 'usuarios'

router = routers.DefaultRouter()

router.register(r'usuarios', UserViewSet, basename="usuarios")


urlpatterns = [
    path('', include(router.urls)),
]
