from django.shortcuts import render,redirect
from .forms import albumForm
from .models import albumModel
# Create your views here.


def addAlbum(request):
    if request.method=="POST":
        form=albumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addAlbum')
    else:
        form=albumForm()
    return render(request,'addAlbum.html',{'data':form})

def editAlbum(request,id):
    name=albumModel.objects.get(pk=id)
    form=albumForm(instance=name)
    if request.method=="POST":
        form=albumForm(request.POST,instance=name)
        if form.is_valid():
            form.save()
            return redirect ('homepage')
    return render(request,'addAlbum.html',{'data':form})

def deleteAlbum(request,id):
        name=albumModel.objects.get(pk=id)
        name.delete()
        return redirect('homepage')