from django.urls import path
from . import views


urlpatterns = [
    path('addMusician/',views.AddMusician.as_view(),name='addMusician'),
    path('editMusician/<int:pk>/',views.EditMusician.as_view(),name='editMusician'),
    path('register/', views.register, name='register'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
