from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
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
    
    def test_menu_html_rendering(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, "<h1>Menu</h1>")
        self.assertContains(response, "Pizza")  
        self.assertContains(response, "Pasta")

    def test_about_view(self):
        """Test about page rendering"""
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_home_view(self):
        """Test home page rendering"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
