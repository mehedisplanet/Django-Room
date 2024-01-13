from django.shortcuts import render
from album.models import albumModel
from musician.models import musicianModel

def home(request):
    # data_1=musicianModel.objects.all()
    data_2=albumModel.objects.all()
    # data= list(data_1) + list(data_2)
    # print(data)
    return render(request,'home.html',{'data': data_2})