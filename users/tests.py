from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User


class UserAPITest(APITestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "phone": "123456789",
            "avatar": None,
            "country": "Test Country",
            "comment": "Test comment",
            "first_name": "Test",
            "last_name": "User",
            "is_active": True,
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_create_user(self):
        url = reverse("user_create")
        response = self.client.post(url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_get_user_list(self):
        url = reverse("user_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_user_detail(self):
        url = reverse("user_deteil", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.user.email)

    def test_update_user(self):
        url = reverse("user_update", args=[self.user.id])
        updated_data = {
            "email": "updated@example.com",
            "phone": "987654321",
            "avatar": None,
            "country": "Updated Country",
            "comment": "Updated comment",
            "first_name": "Updated",
            "last_name": "User",
            "is_active": False,
        }
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, updated_data["email"])

    def test_delete_user(self):
        url = reverse("user_delete", args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.count(), 0)
