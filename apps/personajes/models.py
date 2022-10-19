from django.db import models


class Raza(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre


class Personaje(models.Model):
    SEXO =  [
        ('1', 'Femenino'),
        ('2', 'Masculino'),
        ('3', 'Ninguno'),
    ]
    nombre = models.CharField(max_length=100)
    actor_nombre = models.CharField(max_length=100, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO, null=True, blank=True)
    raza = models.ForeignKey(Raza, on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return self.nombre
    