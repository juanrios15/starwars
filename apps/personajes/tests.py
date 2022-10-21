import json

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient

from .models import Raza, Personaje


class PersonajesTestCase(TestCase):    
    
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
        
        raza1 = Raza(nombre='Humano')
        raza1.save()
        
        personaje1 = Personaje(nombre='Luke Skywalker',actor_nombre='Mark Hamill', sexo=2, raza=raza1)
        personaje1.save()
        
    def test_get_personajes(self):
        user = User.objects.get(username='testing')
        client = APIClient()
        client.force_authenticate(user=user)
        response = client.get("/personajes/personajes/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_personajes_noauth(self):
        client = APIClient()
        response = client.get("/personajes/personajes/")
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(result["detail"], "Authentication credentials were not provided.")
        

    def test_post_personajes(self):
        user = User.objects.get(username='testing')
        client = APIClient()
        client.force_authenticate(user=user)
        data = {'nombre': 'Han Solo', 'actor_nombre':'Tom Hanks', 'sexo': '2', 'raza':1}
        response = client.post("/personajes/personajes/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = json.loads(response.content)
        if 'id' in result:
            del result['id']
        self.assertEqual(result, data)