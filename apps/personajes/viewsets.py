from rest_framework import viewsets

from .models import Raza, Personaje
from .serializers import RazaSerializer, PersonajeSerializer


class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer


class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer
