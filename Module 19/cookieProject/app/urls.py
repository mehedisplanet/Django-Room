from django.urls import path
from . import views

urlpatterns = [
    path('',views.set_session),
    path('get/',views.get_cookie),
    path('set/',views.get_session),
    path('delete/',views.delete_cookie),
    path('del/',views.delete_session),
]
