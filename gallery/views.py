from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Gallery, Location, categories

# Create your views here.
def welcome(request):
    pic_categories = categories.objects.all()
    all_gallery = Gallery.objects.all()
    return render( request, 'welcome.html', {"pic_categories": pic_categories, "all_gallery": all_gallery})

def picture_category(request):
    date = dt.date.today()
    return render(request, 'all-pics/category-pics.html', {"date": date,})

def picture_location(request):
    date = dt.date.today()
    return render(request, 'all-pics/location-pics.html', {"date": date,})

