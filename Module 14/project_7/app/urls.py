from django.urls import path
# from . import views
from app.views import home


urlpatterns = [
    # path('',views.home,name='homepage') // 2 ar 7 ak sathe cholbe
    path('',home,name='homepage')
]
