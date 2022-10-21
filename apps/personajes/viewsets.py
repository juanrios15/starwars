from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import Raza, Personaje
from .serializers import RazaSerializer, PersonajeSerializer, GetPersonajeSerializer

class RazaViewSet(viewsets.ModelViewSet):
    queryset = Raza.objects.all()
    serializer_class = RazaSerializer


class PersonajeViewSet(viewsets.ModelViewSet):
    queryset = Personaje.objects.all()
    serializer_class = PersonajeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'nombre': ('exact', 'icontains'),
    }
    
    def get_serializer_class(self):
        serializer_class = self.serializer_class
        if self.action == 'list' or self.action == 'retrieve':
            serializer_class = GetPersonajeSerializer
        return serializer_class
