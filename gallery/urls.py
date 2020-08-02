from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url('^category/$', views.picture_category, name='pictureCategory'),
    url('^location/$', views.picture_location, name ='pictureLocation'),
    url(r'^search/', views.search_results, name='search_results')
]