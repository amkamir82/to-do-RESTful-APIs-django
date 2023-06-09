from django.test import TestCase
from todo.models.user import User
from django.urls import reverse
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


class AddProjectAPITest(APITestCase):

    def setUp(self):
        self.manager = User.objects.create_user(
            username='manager',
            password='password123',
            email='manager@example.com',
            role='Project Manager'
        )
        self.client.force_authenticate(user=self.manager)

    def test_add_project_as_manager(self):
        url = reverse('add_project')
        data = {
            'name': 'Project 1',
            'description': 'This is project 1'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Project 1')
        self.assertEqual(response.data['description'], 'This is project 1')

    def test_add_project_as_developer(self):
        developer = User.objects.create_user(
            username='developer',
            password='password123',
            email='developer@example.com',
            role='Developer'
        )
        self.client.force_authenticate(user=developer)

        url = reverse('add_project')
        data = {
            'name': 'Project 2',
            'description': 'This is project 2'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
