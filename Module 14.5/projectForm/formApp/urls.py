from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='homepage'),
    path('studentForm/',views.studentForm,name='studentForm'),
    path('officeForm/',views.officeForm,name='officeForm'),
    path('passwordForm/',views.passwordForm,name='passwordForm'),
    path('studentInformation/',views.studentInformation,name='studentInformation'),
]
