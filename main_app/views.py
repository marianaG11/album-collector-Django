from django.shortcuts import render, redirect

#import CreateView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Add the following import
from django.http import HttpResponse
from .models import Album, Listener, Photo
#import the SongForm
from .forms import SongForm
#for the login function
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required
#boto3 library
import boto3

#import uuid utility to generate random strings
import uuid

#add constant variables to be able to use aws
S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'catcollectormarianag'

class AlbumCreate(LoginRequiredMixin, CreateView):
	model = Album
	fields = ['name', 'artist_name', 'number_of_songs', 'genre', 'release_year']
	#this inherited method is called when a valid album form is submitted
	def form_valid(self,form):
		form.instance.user = self.request.user #form.instance is the album
		return super().form_valid(form)
 
 
 

class AlbumUpdate(LoginRequiredMixin, UpdateView):
	model = Album
	fields = ['artist_name', 'number_of_songs', 'genre', 'release_date']

class AlbumDelete(LoginRequiredMixin, DeleteView):
	model = Album
	#redirect back to the albums index page since the album doesn't exists anymore
	success_url = '/albums/' 
	

def signup(request):

	error_message = ""
    
	if request.method == 'POST':
		# This is how to create a 'user' form object
		# that includes the data from the browser
		#on a post lets signup the user and log them in
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save() #this saves the user to the DB
			#login takes two arguments of request and user
			login(request, user)#now the user is logged in and available on every request
			return redirect('index')
		else:
			error_message = 'Invalid sign up - try again'
	# A bad POST or a GET request, so render signup.html with an empty form
	form = UserCreationForm()
	context = {'form': form, 'error_message': error_message}
	return render(request, 'registration/signup.html', context) #rendering out a template



# Create your views here.
# Define the home view
def home(request):
	return render(request, 'home.html')

def about(request):
	return render(request, 'about.html')

@login_required
def albums_index(request):
	albums = Album.objects.filter(user=request.user) #to only show the logged in User's albums
	return render(request, 'albums/index.html', {'albums': albums})


@login_required
def albums_detail(request, album_id):
	album = Album.objects.get(id=album_id)
	#get the listeners the album doesnt have
	listeners_album_doesnt_have = Listener.objects.exclude(id__in = album.listeners.all().values_list('id'))
	#instantiate SongForm to be rendered in the template
	song_form = SongForm()
	return render(request, 'albums/detail.html', {
		#include the album and the song_form in the context
		'album': album, 'song_form': song_form, 'listeners': listeners_album_doesnt_have})

@login_required
def add_song(request, album_id):
	
	form = SongForm(request.POST)
	if form.is_valid():
		new_song = form.save(commit=False)
		new_song.album_id = album_id
		new_song.save()
	
	return redirect('detail', album_id=album_id)

@login_required
def assoc_listener(request, album_id, listener_id):
    #can pass in a listeners id instead of the whole object
	Album.objects.get(id=album_id).listeners.add(listener_id)
	return redirect('detail', album_id=album_id)


@login_required
def add_photo(request, album_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to album_id or album
            Photo.objects.create(url=url, album_id=album_id)
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', album_id=album_id)


class ListenerList(LoginRequiredMixin, ListView):
    model = Listener

class ListenerDetail(LoginRequiredMixin, DetailView):
    model = Listener
    
class ListenerCreate(LoginRequiredMixin, CreateView):
    model = Listener
    fields = '__all__'
    
class ListenerUpdate(LoginRequiredMixin, UpdateView):
    model = Listener
    fields = ['name', 'location']
    
class ListenerDelete(LoginRequiredMixin, DeleteView):
    model = Listener
    success_url = '/listeners/'