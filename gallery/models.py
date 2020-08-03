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
    image = models.ImageField(upload_to = 'pictures/')
    location = models.ForeignKey(Location, default='unknown', on_delete = models.DO_NOTHING)
    categories = models.ManyToManyField(categories, related_name='galleries')
    save_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
    
    def save_gallery(self):
        self.save()
    
    @classmethod
    def search_by_category(cls, search_term):
        pictures = cls.objects.filter(categories__category_name__icontains=search_term)
        return pictures
    class Meta:
        ordering = ['image_name']