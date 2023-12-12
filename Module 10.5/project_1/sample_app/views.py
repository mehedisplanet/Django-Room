from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.


def home(request):
    return render(request, 'sample_app/index.html')


def about(request):
    return render(request, 'sample_app/about.html')


def contact(request):
    return render(request, 'sample_app/contact.html')


def filter(request):
    d = {'name': "Mehedi Hasan",
         'age': 27,
         'gender': 'male',
         'religion': 'Islam',
         'birthday': datetime.datetime.now(),
         'lst': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
         'slogan': 'Python is best programming language',
         'empty': '',
         'courses': [
             {'id': 1, 'name': 'Python', 'fee': 5000},
             {'id': 2, 'name': 'C++', 'fee': 2000},
             {'id': 3, 'name': 'JavaScript', 'fee': 1500}
         ],
         'student': [
             {'name': 'zed', 'age': 19},
             {'name': 'amy', 'age': 22},
             {'name': 'joe', 'age': 31},
             {'name': 'rahat', 'age': 15},
             {'name': 'mia', 'age': 24},
             {'name': 'rakib', 'age': 27},
         ]
         }
    return render(request, 'sample_app/filter.html', context=d)
