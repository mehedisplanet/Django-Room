from django.shortcuts import render, redirect
from .forms import AuthorForm
# Create your views here.


def addAuthor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addAuthor')
    else:
        form = AuthorForm()
    return render(request, 'addAuthor.html', {'data': form})
