from django.urls import path
from . import views

urlpatterns = [
    path('addAlbum/',views.AddAlbum.as_view(),name='addAlbum'),
    path('editAlbum/<int:pk>',views.EditAlbum.as_view(),name='editAlbum'),
    path('deleteAlbum/<int:pk>',views.DeleteAlbumView.as_view(),name='deleteAlbum')
]
