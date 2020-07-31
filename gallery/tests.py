from django.test import TestCase
from .models import Gallery, categories, Location

class GalleryTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.location1 = Location(location_name='location1')
        self.gallary1 = Gallery(image_name='image1', image_description='image description 1', image = 'picture/image1', location=self.location1)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.gallary1, Gallery))