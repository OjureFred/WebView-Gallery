from django.test import TestCase
from .models import Gallery, categories, Location

class GalleryTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.location1 = Location(location_name='location1')
        self.gallery1 = Gallery(image_name='image1', image_description='image description 1', image = 'picture/image1', location=self.location1)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.gallery1, Gallery))
    
    #Testing the save method
    def test_save_method(self):
        self.location1.save_location()
        self.gallery1.save_gallery()
        galleries = Gallery.objects.all()
        self.assertTrue(len(galleries)> 0)