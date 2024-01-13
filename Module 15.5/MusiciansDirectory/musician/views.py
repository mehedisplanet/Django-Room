from django.shortcuts import render,redirect
from .forms import musicianForm
from .models import musicianModel

# Create your views here.


def addMusician(request):
    if request.method=="POST":
        form=musicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('addMusician')
    else:
        form=musicianForm()
    return render(request,'addMusician.html',{'data':form})

def editMusician(request,id):
    name=musicianModel.objects.get(pk=id)
    form=musicianForm(instance=name)
    if request.method=="POST":
        form=musicianForm(request.POST,instance=name)
        if form.is_valid():
            form.save()
            return redirect ('homepage')
    return render(request,'addMusician.html',{'data':form})

def deleteMusician(request,id):
        name=musicianModel.objects.get(pk=id)
        name.delete()
        return redirect('homepage')