from django.urls import path
from . import views

urlpatterns = [
    path('addAlbum/',views.addAlbum,name='addAlbum'),
    path('editAlbum/<int:id>',views.editAlbum,name='editAlbum'),
    path('deleteAlbum/<int:id>',views.deleteAlbum,name='deleteAlbum')
]
