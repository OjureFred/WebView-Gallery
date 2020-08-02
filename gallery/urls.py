from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url('^category/$', views.picture_category, name='pictureCategory'),
    url('^location/$', views.picture_location, name ='pictureLocation'),
    url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)