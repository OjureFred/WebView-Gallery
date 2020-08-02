from django.db import models

# Create your models here.
class categories(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name

class Location(models.Model):
    location_name = models.CharField(max_length=50, default='unknown')

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

class Gallery(models.Model):
    image_name = models.CharField(max_length=50)
    image_description = models.TextField()
    image = models.ImageField(upload_to = 'pictures/', blank=True)
    location = models.ForeignKey(Location, default='unknown', on_delete = models.DO_NOTHING)
    categories = models.ManyToManyField(categories)
    save_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
    
    def save_gallery(self):
        self.save()
    
    class Meta:
        ordering = ['image_name']