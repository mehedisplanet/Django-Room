from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is HOME page")
def index(request):
    return render(request,"first_app/home.html")