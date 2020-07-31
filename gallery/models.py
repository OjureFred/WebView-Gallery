from django.db import models

# Create your models here.
class Gallery(models.Model):
    image_name = models.CharField(max_length=50)
    image_description = models.CharField(max_length=250)
    image_location = models.ForeignKey(Location)
    categories = models.ManyToManyField(categories)
    save_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']

class categories(models.Model):
    category_name = models.CharField(max_length=50)

class Location(models.Model):
    location_name = models.CharField(max_length=50)
