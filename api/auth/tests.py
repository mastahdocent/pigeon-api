from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

User = get_user_model()

ENDPOINT = "http://127.0.0.1:8000/"

class RegisterTests(APITestCase):
    def test_create_user(self):
        url = ENDPOINT + "auth/register/"
        data = {
            "username": "test_user",
            "password": "testpass123",
            "password2": "testpass123",
            "email": "test@test.com"
        }
        response = self.client.post(url, data, format="json")

        # assert user was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # assert only one user was created and it contains valid data
        qs = User.objects.all()
        user = qs.get(username="test_user")
        self.assertEqual(qs.count(), 1)
        self.assertEqual(user.email, "test@test.com")

class AuthTests(APITestCase):
    def setUp(self):
        test_user = User.objects.create(
            username="test_user",
            email="test@test.com"
        )
        test_user.set_password("testpass123")
        test_user.save()
        self.test_user = test_user

    def test_auth_username(self):
        url = ENDPOINT + "auth/login/"
        data = {
            "username": "test_user",
            "password": "testpass123"
        }
        response = self.client.post(url, data, format="json")

        # assert login successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("user"), "test_user")

    def test_auth_email(self):
        url = ENDPOINT + "auth/login/"
        data = {
            "username": "test@test.com",
            "password": "testpass123"
        }
        response = self.client.post(url, data, format="json")

        # assert login successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("user"), "test_user")