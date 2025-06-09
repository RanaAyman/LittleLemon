from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(TestCase):

    def setUp(self):
        """Add test instances of the Menu model"""
        self.item1 = MenuItem.objects.create(title="Pizza", price=150, inventory=50)
        self.item2 = MenuItem.objects.create(title="Pasta", price=120, inventory=40)
        self.client = APIClient()
        
        """Create a test user and authenticate the client"""
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpassword")  # For SessionAuthentication
        
        # Generate a token for TokenAuthentication
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

    def test_getall(self):
        """Retrieve all Menu objects and verify serialization"""
        response = self.client.get(reverse('menu-list'))  # Update with correct URL name
        menu_items = MenuItem.objects.all()
        expected_data = MenuItemSerializer(menu_items, many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_data)
