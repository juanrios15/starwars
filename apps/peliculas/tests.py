import json

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient

from .models import Planeta, Productor, Director, Pelicula
from apps.personajes.models import Personaje


class PeliculasTestCase(TestCase):    
    
    def setUp(self):
        user = User(
            email='testing@tests.com',
            first_name='Testing',
            last_name='Testing',
            username='testing'
        )
        user.set_password('1234')
        user.save()  
        self.user = user
        
        planeta1 = Planeta(nombre='Marte')
        planeta1.save()
        
        director1 = Director(nombre='George Lucas')
        director1.save()
        
        productor1 = Productor(nombre='Ron Howard')
        productor1.save()
        
        personaje1 = Personaje(nombre='Luke Skywalker',actor_nombre='Mark Hamill', sexo=2)
        personaje1.save()
        
        pelicula1 = Pelicula(
            nombre="Star wars 2",
            resumen="Resumen de la pelicula",
            estreno="1980-05-15",
            duracion=102,
            director=director1,
        )
        pelicula1.save()
        pelicula1.productores.add(productor1)
        pelicula1.personajes.add(personaje1)
        pelicula1.save()
        
    def test_get_planetas(self):
        user = User.objects.get(username='testing')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get("/peliculas/planetas/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_planetas_noauth(self):
        client = APIClient()
        response = client.get("/peliculas/planetas/")
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(result["detail"], "Authentication credentials were not provided.")

    def test_post_planetas(self):
        user = User.objects.get(username='testing')
        client = APIClient()
        client.force_authenticate(user=user)
        data = {'nombre': 'Tierra'}
        response = client.post("/peliculas/planetas/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = json.loads(response.content)
        if 'id' in result:
            del result['id']
        self.assertEqual(result, data)
    
    def test_get_peliculas(self):
        user = User.objects.get(username='testing')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get("/peliculas/peliculas/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_post_peliculas(self):
        user = User.objects.get(username='testing')
        client = APIClient()
        client.force_authenticate(user=user)
        data = {
                'nombre': 'Star Wars',
                'resumen': 'Este es el resumen de la pelicula',
                'estreno': '1977-05-25',
                'duracion': 121,
                'director': 1,
                'productores':[1],
                'personajes':[1],
                'planetas':[1]
            }
        response = client.post("/peliculas/peliculas/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = json.loads(response.content)
        if 'id' in result:
            del result['id']
        self.assertEqual(result, data)
    