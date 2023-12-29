from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homePage'), 
    path('signUp/',views.signUp,name='signUp'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogOut,name='logout'),
    path('passChange/',views.passChange,name='passChange'),
    path('passChange2/',views.passChange2,name='passChange2'),
    path('userChange/',views.userChange,name='userChange'),
    path('profile/',views.profile,name='profile'),
]
