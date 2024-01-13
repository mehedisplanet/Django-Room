from django.http import HttpResponse

def home(request):
    return HttpResponse("This is HOME Page")
def contact(request):
    return HttpResponse("This is CONTACT Page")
def about(request):
    return HttpResponse("This is ABOUT Page")
def media(request):
    return HttpResponse("This is SOCIAL MEDIA Page")