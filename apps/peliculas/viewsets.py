from rest_framework import viewsets

from .models import Planeta, Director, Productor, Pelicula
from .serializers import PlanetaSerializer, DirectorSerializer, ProductorSerializer, PeliculaSerializer


class PlanetaViewSet(viewsets.ModelViewSet):
    queryset = Planeta.objects.all()
    serializer_class = PlanetaSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ProductorViewSet(viewsets.ModelViewSet):
    queryset = Productor.objects.all()
    serializer_class = ProductorSerializer


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
