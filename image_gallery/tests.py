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

    def test_save_location(self):
        self.location.save_location()
        locations=Location.objects.all()
        self.assertTrue(len(locations)> 0)

    def test_delete_location(self):
        self.location.delete_location()
        place=Location.objects.all()
        self.assertTrue(len(place) == 0)

    # def test_update_location(self):
    #     new_location = 'Kisumu'
    #     self.location.update_location(self.location.id, new_location)
    #     changed_location = Location.objects.filter(name='Kisumu')
    #     self.assertEqual(self.location, changed_location)



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

    def test_delete_category(self):
        self.category.delete_category()
        categories=Category.objects.all()
        self.assertTrue(len(categories) == 0)

    class TestImage(TestCase):

        def setUp(self):
            self.location = Location(name='Nairobi')
            self.location.save_location()

            self.category = Category(name='Garden')
            self.category.save_category()

            self.image_test = Image(id=1, name='image', description='this is a test image', location=self.location,
                                    category=self.category)

        def test_instance(self):
            self.assertTrue(isinstance(self.image_test, Image))

        def test_save_image(self):
            self.image_test.save()
            saved_image = Image.objects.all()
            self.assertTrue(len(saved_image) > 0)

        def tearDown(self):
            Image.objects.all().delete()
            Location.objects.all().delete()
            Category.objects.all().delete()

        def test_delete_image(self):
            self.image_test.delete_image()
            pictures = Image.objects.all()
            self.assertTrue(len(pictures) == 0)