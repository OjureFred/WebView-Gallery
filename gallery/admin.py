from django.contrib import admin
from .models import Gallery, Location, categories

# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories',)

    
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Location)
admin.site.register(categories)
