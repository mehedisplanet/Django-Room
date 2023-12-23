from django.shortcuts import render
from .forms import ModelForm

def home(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = ModelForm()  
    return render(request, 'home.html', {'form': form})