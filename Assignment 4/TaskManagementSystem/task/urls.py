from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name="addTask"),
    path('editTask/<int:id>',views.editTask,name="editTask"),
    path('deleteTask/<int:id>',views.deleteTask,name="deleteTask"),
]
