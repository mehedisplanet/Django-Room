from django.urls import path
from . import views

urlpatterns = [
    path('addProfile/', views.addProfile,name='addProfile'),
]
