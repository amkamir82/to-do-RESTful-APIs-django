from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class SignupAPITest(APITestCase):

    def test_signup_as_developer(self):
        url = 'todo/signup/'
        data = {
            'username': 'developer',
            'password': 'password123',
            'email': 'developer@example.com',
            'role': 'Developer'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'developer')

    def test_signup_as_project_manager(self):
        url = 'todo/signup/'
        data = {
            'username': 'manager',
            'password': 'password123',
            'email': 'manager@example.com',
            'role': 'Project Manager'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'manager')
