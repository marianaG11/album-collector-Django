
from django.forms import ModelForm 
from .models import Song

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['name', 'minutes']