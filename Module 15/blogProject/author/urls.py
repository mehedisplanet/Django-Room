from django.urls import path
from . import views

urlpatterns = [
    path('addAuthor/', views.addAuthor,name='addAuthor'),
]
