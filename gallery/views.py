from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def welcome(request):
    return render( request, 'welcome.html')

def picture_category(request):
    date = dt.date.today()
    return render(request, 'all-pics/category-pics.html', {"date": date,})

def picture_location(request):
    date = dt.date.today()
    return render(request, 'all-pics/location-pics.html', {"date": date,})

