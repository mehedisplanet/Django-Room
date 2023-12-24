from django.urls import path
from . import views

urlpatterns = [
    path('addPost/', views.addPost,name='addPost'),
    path('editPost/<int:id>', views.editPost,name='editPost'),
    path('deletePost/<int:id>', views.deletePost,name='deletePost'),
]
