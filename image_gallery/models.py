
from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=40)

class Category(models.Model):
    name = models.CharField(max_length=40)

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.TextField()
    photographer = models.CharField(max_length=40, default='admin')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
