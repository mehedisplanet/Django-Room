from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("This is FIRST_APP HOME page")
def courses(request):
    return HttpResponse("This is FIRST_APP COURSES page")
def about(request):
    return HttpResponse("This is FIRST_APP ABOUT page")
def media(request):
    return HttpResponse("This is FIRST_APP MEDIA page")