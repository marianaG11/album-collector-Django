from django.db import models

#import the reverse function
from django.urls import reverse
# Create your models here.
class Album(models.Model): 
    name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    number_of_songs = models.IntegerField()
    genre = models.TextField(max_length=100)
    release_date = models.IntegerField()

    def __str__(self): 
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'album_id': self.id})