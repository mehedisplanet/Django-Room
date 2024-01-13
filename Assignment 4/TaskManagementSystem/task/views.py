from django.shortcuts import render,redirect
from .forms import taskForm
from .models import taskModel

# Create your views here.

def addTask(request):
    if request.method=="POST":
        form=taskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form=taskForm()
    return render(request,'addTask.html',{'data':form})

def editTask(request,id):
    root=taskModel.objects.get(pk=id)
    form=taskForm(instance=root)
    if request.method=="POST":
        form=taskForm(request.POST,instance=root)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,'addTask.html',{'data':form})

def deleteTask(request,id):
    root=taskModel.objects.get(pk=id)
    root.delete()
    return redirect('homepage')