from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(request,'base.html')


def ordinaryCodes(request):
    if request.method == "POST":
        data = forms.ExampleForm(request.POST)
        if data.is_valid():
            print(data.cleaned_data)
        return render(request, 'ordinaryCodes.html', {'data': data})
    else:
        data = forms.ExampleForm()
        return render(request, 'ordinaryCodes.html', {'data': data})
    
def geeksForGeeks(request):
    if request.method=="POST":
        data=forms.GeeksForm(request.POST)
        if data.is_valid():
            print(data.cleaned_data)
        return render (request,'geeksForGeeks.html',{'data':data})
    else:
        data=forms.GeeksForm()
        return render (request,'geeksForGeeks.html',{'data':data})
