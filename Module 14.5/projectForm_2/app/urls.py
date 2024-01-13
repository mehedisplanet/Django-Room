from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('OrdinaryCodes/',views.ordinaryCodes,name='ordinaryCodes'),
    path('geeksForGeeks/',views.geeksForGeeks,name='geeksForGeeks')
]
