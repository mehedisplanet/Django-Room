from django.shortcuts import render
from . forms import contactForm, StudentData, passwordMatching

# Create your views here.

def home(request):
    return render(request, 'app/home.html')


def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        select = request.POST.get('select')
        return render(request, 'app/about.html', {'name': name, 'email': email, 'select': select})
    else:
        return render(request, 'app/about.html')


def submitForm(request):
    return render(request, 'app/form.html')


def djangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            # print('File Upload Successfully')
            print(form.cleaned_data)
        return render(request, 'app/djangoForm.html', {'form': form})
    else:
        form = contactForm()
        return render(request, 'app/djangoForm.html', {'form': form})


def studentForm(request):
    if request.method == 'POST':
        form = StudentData(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print('File Upload Successfully')
            print(form.cleaned_data)
        return render(request, 'app/djangoForm.html', {'form': form})
    else:
        form = StudentData()
        return render(request, 'app/djangoForm.html', {'form': form})


def passwordForm(request):
    if request.method == 'POST':
        form = passwordMatching(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
        return render(request, 'app/djangoForm.html', {'form': form})
    else:
        form = passwordMatching()
        return render(request, 'app/djangoForm.html', {'form': form})
