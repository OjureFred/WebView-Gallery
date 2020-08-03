from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Gallery, Location, categories

# Create your views here.
def welcome(request):
    all_gallery = Gallery.objects.all()
    return render( request, 'welcome.html', {"all_gallery": all_gallery})

def picture_category(request):
    date = dt.date.today()
    return render(request, 'all-pics/category-pics.html', {"date": date,})

def picture_location(request):
    date = dt.date.today()
    return render(request, 'all-pics/location-pics.html', {"date": date,})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Gallery.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/category-pics.html', {"message": message, "pictures": searched_category})
    
    else:
        message = "You haven't searched for any category"
        return render(request, 'all-pics/category-pics.html', {"message": message})

def gallery(request, gallery_id):
    try:
        gallery = Gallery.objects.get(id=gallery_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-pics/gallery.html", {"gallery": gallery})

