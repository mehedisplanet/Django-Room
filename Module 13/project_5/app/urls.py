from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('submitForm/',views.submitForm,name='submitForm'),
    # path('djangoForm/',views.djangoForm,name='djangoForm'),
    # path('djangoForm/',views.studentForm,name='djangoForm'),
    path('djangoForm/',views.passwordForm,name='djangoForm'),
]
