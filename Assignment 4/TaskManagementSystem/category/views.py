from django.shortcuts import render,redirect
from .forms import categoryForm

# Create your views here.

def addCategory(request):
    if request.method=="POST":
        form=categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addCategory')
    else:
        form=categoryForm()
    return render(request,'addCategory.html',{'data':form})