from django.shortcuts import render
from album.models import albumModel
from musician.models import musicianModel

def home(request):
    data_2=albumModel.objects.all()
    return render(request,'home.html',{'data': data_2})