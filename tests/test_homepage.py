from django.test import TestCase
from django.urls import reverse

class HomepageTest(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))  # Assuming 'home' is the name of your homepage URL
        self.assertEqual(response.status_code, 200)  # Check if the response status code is 200 (OK)
