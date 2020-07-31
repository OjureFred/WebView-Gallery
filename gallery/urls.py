from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.welcome, name='welcome'),
    url('^category/$', views.picture_category, name='pictureCategory'),
    url('^location/$', views.picture_location, name ='pictureLocation')
]