
from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(image=value)
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    photographer = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    # Save image
    def save_image(self):
        self.save()

    def delete(self):
        self.delete()
        


