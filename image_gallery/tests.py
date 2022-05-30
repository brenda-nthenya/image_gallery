from django.test import TestCase
from .models import *

# Create your tests here.
class TestLocation(TestCase):

    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))