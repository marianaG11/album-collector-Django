from django.shortcuts import render

#import CreateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Add the following import
from django.http import HttpResponse

from .models import Album

class AlbumCreate(CreateView):
	model = Album 
	fields = '__all__'

class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist_name', 'number_of_songs', 'genre', 'release_date']

class AlbumDelete(DeleteView):
	model = Album
	#redirect back to the albums index page since the album doesnt exists anymore
	success_url = '/albums/' 
	







# Create your views here.
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
    