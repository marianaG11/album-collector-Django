from django.contrib import admin

#import models here
from .models import Album, Song
# Register your models here.
admin.site.register(Album)

admin.site.register(Song)
