from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return render( request, 'welcome.html')

def picture_category(request):
    html = f'''
        <html>
            <body> 
                <h1> Displaying pictures of current category </h1>
            </body>
        </html>
        '''
    return HttpResponse(html)

def picture_location(request):
    html = f'''
        <html>
            <body> 
                <h1> Displaying pictures of current location </h1>
            </body>
        </html>
        '''
    return HttpResponse(html)

