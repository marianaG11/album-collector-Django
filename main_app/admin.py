from django.contrib import admin

#import models here
from .models import Album, Song, Listener, Photo
# Register your models here.
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Listener)
admin.site.register(Photo)