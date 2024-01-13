from django.urls import path
from . import views

urlpatterns = [
    path('addCategory/',views.addCategory,name='addCategory'),
]
