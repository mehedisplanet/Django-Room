from django.urls import path
from . import views


urlpatterns = [
    path('addMusician/',views.addMusician,name='addMusician'),
    path('editMusician/<int:id>',views.editMusician,name='editMusician'),
]
