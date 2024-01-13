from django.shortcuts import render, redirect
from .forms import CategoryForm
# Create your views here.


def addCategory(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addCategory')
    else:
        form = CategoryForm()
    return render(request, 'addCategory.html', {'data': form})