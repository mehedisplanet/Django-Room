from django.shortcuts import render, redirect
from .forms import profileForm
# Create your views here.


def addProfile(request):
    if request.method == "POST":
        form = profileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addProfile')
    else:
        form = profileForm()
    return render(request, 'addProfile.html', {'data': form})