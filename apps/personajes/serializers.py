from rest_framework import serializers

from .models import Raza, Personaje
from apps.peliculas.models import Pelicula
from apps.peliculas.serializers import PeliculaSerializer


class RazaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Raza
        fields = '__all__'


class GetPersonajeSerializer(serializers.ModelSerializer):
    peliculas = serializers.SerializerMethodField()
    sexo = serializers.ReadOnlyField(source='get_sexo_display')
    raza = serializers.ReadOnlyField(source='raza.nombre')
    
    class Meta:
        model = Personaje
        fields = '__all__'
    
    def get_peliculas(self, obj):
        peliculas = Pelicula.objects.filter(personajes=obj)
        list_peliculas = []
        for pelicula in peliculas:
            list_peliculas.append(pelicula.nombre)
        return list_peliculas


class PersonajeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Personaje
        fields = '__all__'
