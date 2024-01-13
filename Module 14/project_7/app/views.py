from django.shortcuts import render
from .  import forms

# Create your views here.

def home(request):
    if request.method=='POST':
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print(form.cleaned_data)
    else:
        form=forms.StudentForm()
    return render(request,'app/home.html',{'form':form})

