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


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'
