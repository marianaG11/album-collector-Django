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
    #to update 
    path('albums/<int:pk>/update/', views.AlbumUpdate.as_view(), name='albums_update'),
    #to delete
    path('albums/<int:pk>/delete/', views.AlbumDelete.as_view(), name='albums_delete'), 
    path('albums/<int:album_id>/add_song/', views.add_song, name='add_song'),
    #associate a listener with an album (M:M relationship)
    path('albums/<int:album_id>/assoc_listener/<int:listener_id>/', views.assoc_listener, name='assoc_listener'),
    path('listeners/', views.ListenerList.as_view(), name='listeners_index'),
    path('listeners/<int:pk>/', views.ListenerDetail.as_view(), name='listeners_detail'),
    path('listeners/create/', views.ListenerCreate.as_view(), name='listeners_create'),
    path('listeners/<int:pk>/update/', views.ListenerUpdate.as_view(), name='listeners_update'),
    path('listeners/<int:pk>/delete/', views.ListenerDelete.as_view(), name='listeners_delete'),
    ]