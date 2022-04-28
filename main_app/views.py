from django.shortcuts import render, redirect

#import CreateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Add the following import
from django.http import HttpResponse

from .models import Album, Listener
#import the SongForm
from .forms import SongForm

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
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

def albums_index(request):
	albums = Album.objects.all()
	return render(request, 'albums/index.html', {'albums': albums})

def albums_detail(request, album_id):
	album = Album.objects.get(id=album_id)
	#get the listeners the album doesnt have
	listeners_album_doesnt_have = Listener.objects.exclude(id__in = album.listeners.all().values_list('id'))
	#instantiate SongForm to be rendered in the template
	song_form = SongForm()
	return render(request, 'albums/detail.html', {
		#include the album and the song_form in the context
		'album': album, 'song_form': song_form, 'listeners': listeners_album_doesnt_have})

	
def add_song(request, album_id):
	
	form = SongForm(request.POST)
	if form.is_valid():
		new_song = form.save(commit=False)
		new_song.album_id = album_id
		new_song.save()
	
	return redirect('detail', album_id=album_id)


def assoc_listener(request, album_id, listener_id):
    #can pass in a listeners id instead of the whole object
	Album.objects.get(id=album_id).listeners.add(listener_id)
	return redirect('detail', album_id=album_id)

class ListenerList(ListView):
    model = Listener

class ListenerDetail(DetailView):
    model = Listener
    
class ListenerCreate(CreateView):
    model = Listener
    fields = '__all__'
    
class ListenerUpdate(UpdateView):
    model = Listener
    fields = ['name', 'location']
    
class ListenerDelete(DeleteView):
    model = Listener
    success_url = '/listeners/'