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

def search_results(request):

    if 'location' in request.GET and request.GET["location"]:
        search_term = request.GET.get("location")
        searched_location = Gallery.search_by_location(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/location.html', {"message": message, "pictures": searched_location})
    
    else:
        message = "You haven't searched for any location"
        return render(request, 'all-pics/location.html', { "message": message})

