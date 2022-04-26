from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name = 'about'),
    #route for the albums index
    path('albums/', views.albums_index, name = 'index'),
    path('albums/<int:album_id>/', views.albums_detail, name = 'detail'),
    #to show a form and create an album
    path('albums/create/', views.AlbumCreate.as_view(), name='albums_create'),
]