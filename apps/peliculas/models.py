from django.db import models

from apps.personajes.models import Personaje


class Planeta(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


class Director(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


class Productor(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    nombre = models.CharField(max_length=100)
    resumen = models.CharField(max_length=250, blank=True, null=True)
    estreno = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, blank=True)
    duracion = models.IntegerField(blank=True, null=True)
    productores = models.ManyToManyField(Productor, blank=True)
    planetas = models.ManyToManyField(Planeta, blank=True)
    personajes = models.ManyToManyField(Personaje, blank=True)
    
    
    def __str__(self):
        return self.nombre