from rest_framework import serializers

from .models import Planeta, Director, Productor, Pelicula


class PlanetaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Planeta
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Director
        fields = '__all__'


class ProductorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Productor
        fields = '__all__'


class GetPeliculaSerializer(serializers.ModelSerializer):
    director = serializers.ReadOnlyField(source='director.nombre')
    productores = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre')
    planetas = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre')
    personajes = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre')

    class Meta:
        model = Pelicula
        fields = '__all__'


class PeliculaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pelicula
        fields = '__all__'
