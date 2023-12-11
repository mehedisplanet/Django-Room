from django.shortcuts import render
import datetime
# from django.http import HttpResponse

# Create your views here.

def home(request):
    d={'author':'Rahim','age':5,'lst':['Python','Is','Best'],
       'birthday':datetime.datetime.now(),'value':' ','code':'Coding Fun Have a Nice Day .','courses':[
        {
            'id':1,
            'name':'python',
            'fee':2000,
        },
        {
            'id':2,
            'name':'C++',
            'fee':3000,
        },
        {
            'id':3,
            'name':'JavaScript',
            'fee':5000,
        }
    ]}
    return render(request,'first_app/home.html',d)