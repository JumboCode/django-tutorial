
# Create your tests here.

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Sled

class SledTests(APITestCase):

    # Function run before to populate database for tests
    def setUp(self):
        self.jumbos = Sled.objects.create(name="jumboss")
        self.jumbolinas = Sled.objects.create(name="Jumbolinas")
        self.monaco = Sled.objects.create(name="Mt. Monaco")


    # All tests that are run are pre-pended with test
    def test_list_sleds(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('sled-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 3)


