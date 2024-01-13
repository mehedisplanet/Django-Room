from django.shortcuts import render
from task.models import taskModel


def home(request):
    data=taskModel.objects.all()
    return render (request,'home.html',{'data':data})