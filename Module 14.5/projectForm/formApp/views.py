from django.shortcuts import render
from .  forms import StudentForm,OfficeForm,PasswordMatching

# Create your views here.

def home(request):
    return render(request,'formApp/home.html')

def studentInformation(request):
    if request.method == 'POST':
        print(request.POST)
        roll = request.POST.get('studentRoll')
        name = request.POST.get('studentName')
        father = request.POST.get('fatherName')
        address = request.POST.get('address')
        return render(request, 'formApp/studentInformation.html', {'roll': roll, 'name': name,'father':father, 'address': address})
    else:
        return render(request, 'formApp/studentInformation.html')

def studentForm(request):
    if request.method == "POST":
        std = StudentForm
        if std.is_valid():
            print(std.cleaned_data)
        return render(request, 'formApp/studentForm.html', {'data': std})
    else:
        std = StudentForm()
        return render(request, 'formApp/studentForm.html', {'data': std})

def officeForm(request):
    if request.method=="POST":
        of=OfficeForm(request.POST ,request.FILES)
        if of.is_valid():
            print(of.cleaned_data)
            return render (request,'formApp/officeForm.html',{'data':of})
    else:
        of=OfficeForm()
        return render (request,'formApp/officeForm.html',{'data':of})

def passwordForm(request):
    if request.method=="POST":
        pf=PasswordMatching(request.POST, request.FILES)
        if pf.is_valid():
            print(pf.cleaned_data)
        return render (request,'formApp/passwordForm.html',{'data':pf})
    else:
        pf=PasswordMatching()
        return render (request,'formApp/passwordForm.html',{'data':pf})