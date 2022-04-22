from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

class Album: 
    def __init__(self, name, artist_name, number_of_songs, genre, release_date):
        self.name = name
        self.artist_name = artist_name
        self.number_of_songs = number_of_songs
        self.genre = genre
        self.release_date = release_date

albums = [
    Album('Blonde', 'Frank Ocean', 17, 'R&B', 2016),
    Album('Trilogy', 'The Weeknd', 30, 'R&B/Soul', 2012),
    Album('In Utero', 'Nirvana', 12, 'Grunge, Alternative Rock', 1993)
]







# Define the home view
def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def albums_index(request):
    return render(request, 'albums/index.html', {'albums': albums})
