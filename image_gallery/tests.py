from django.test import TestCase
from .models import *

# Create your tests here.
class TestLocation(TestCase):

    def setUp(self):
        self.location = Location(name='Nairobi')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_get_location(self):
        self.location.save_location()
        locations=Location.get_locations()
        self.assertTrue(len(locations) > 0)

class TestCategory(TestCase):

    def setUp(self):
        self.category = Category(name='home')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories)> 0)