from django.urls import path
from . import views


urlpatterns = [
    path('signUp/',views.signUp,name='signUp'),
    path('login/',views.userLogin,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logOut/',views.logOut,name='logOut'),
    path('passChange/',views.passChange,name='passChange'),
    path('passChange2/',views.passChange2,name='passChange2'),
]
