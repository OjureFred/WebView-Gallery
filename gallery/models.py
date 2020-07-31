from django.db import models

# Create your models here.
class Gallery(models.Model):
    image = model.ImaageField(upload_to='images')
