from django.urls import path, include
from rest_framework import routers

from .viewsets import RazaViewSet, PersonajeViewSet

app_name = 'personajes'

router = routers.DefaultRouter()

router.register(r'razas', RazaViewSet, basename="razas")
router.register(r'personajes', PersonajeViewSet, basename="personajes")


urlpatterns = [
    path('', include(router.urls)),
]
