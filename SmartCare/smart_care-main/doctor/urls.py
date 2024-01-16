from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('list', views.DoctorViewSet) # router er antenna
router.register('specialization', views.SpecializationViewSet) # router er antenna
router.register('available_time', views.AvailableTimeViewSet) # router er antenna
router.register('designation', views.DesignationViewSet) # router er antenna
router.register('reviews', views.ReviewViewSet) # router er antenna

urlpatterns = [
    path('', include(router.urls)),
]