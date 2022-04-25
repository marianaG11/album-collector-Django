from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

from .models import Album




# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def albums_index(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})

def albums_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    return render(request, 'albums/detail.html',{'album': album})
    