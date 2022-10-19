from django.urls import path, include
from rest_framework import routers

from .viewsets import PlanetaViewSet, DirectorViewSet, ProductorViewSet, PeliculaViewSet

app_name = 'personajes'

router = routers.DefaultRouter()

router.register(r'planetas', PlanetaViewSet, basename="planetas")
router.register(r'directores', DirectorViewSet, basename="directores")
router.register(r'productores', ProductorViewSet, basename="productores")
router.register(r'peliculas', PeliculaViewSet, basename="peliculas")


urlpatterns = [
    path('', include(router.urls)),
]
