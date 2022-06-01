from django.db import models

#import the reverse function
from django.urls import reverse
# Create your models here.

class Listener(models.Model):
	name = models.CharField(max_length=50)
	location = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('listeners_detail', kwargs={'pk': self.id})
    




class Album(models.Model): 
	name = models.CharField(max_length=100)
	artist_name = models.CharField(max_length=100)
	number_of_songs = models.IntegerField()
	genre = models.TextField(max_length=100)
	release_date = models.IntegerField()
	listeners = models.ManyToManyField(Listener)
 
	def __str__(self): 
		return self.name

	def get_absolute_url(self):
		return reverse('detail', kwargs={'album_id': self.id})


class Song(models.Model):
	name = models.CharField(max_length=100)
	minutes = models.CharField(max_length=100)

	#create an album_id FK
	#FK field type is used to create a 1:M relationship
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
    
	# def __str__(self):
	#     return f"{self.get_minutes_display()} on {self.name}"
 
class Photo(models.Model):
    url = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for album_id: {self.album_id} @{self.url}"
