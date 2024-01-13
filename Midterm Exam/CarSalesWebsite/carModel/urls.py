from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:pk>/', views.DetailsPostView.as_view(), name='details_post'),
    path('carBuy/<int:id>/', views.purchase, name='carBuy'),
]
