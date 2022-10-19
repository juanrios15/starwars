from rest_framework import serializers

from .models import Raza, Personaje
from apps.peliculas.models import Pelicula
from apps.peliculas.serializers import PeliculaSerializer


class RazaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raza
        fields = '__all__'


class PersonajeSerializer(serializers.ModelSerializer):
    peliculas = serializers.SerializerMethodField()
    
    class Meta:
        model = Personaje
        fields = '__all__'
    
    def get_peliculas(self, obj):
        peliculas = Pelicula.objects.filter(personajes=obj)
        list_peliculas = []
        for pelicula in peliculas:
            peli_serializer = PeliculaSerializer(pelicula).data
            list_peliculas.append(peli_serializer)
        return list_peliculas
        