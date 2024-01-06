from django.shortcuts import render
from datetime import datetime,timedelta
from django.http import HttpResponse
# Create your views here.

def home(request):
    response=render(request,'home.html')
    response.set_cookie('name','mehedi',expires=datetime.utcnow()+timedelta(days=10))
    return response

def get_cookie(request):
    name=request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})

def delete_cookie(request):
    response=render(request,'delete_cookie.html')
    response.delete_cookie('name')
    response.delete_cookie('log')
    response.delete_cookie('age')
    return response


#session

def set_session(request):
    data={
        'name':'mehedi',
        'age':27,
        'language':'Bangla'
    }
    request.session.update(data)
    return render(request,'home.html')

def get_session(request):
    if 'name' in request.session:
     name=request.session.get('name','guest')
     request.session.modified=True
     return render (request,'get_session.html',{'name':name})
    else:
        return HttpResponse('Your Session Is Expire')

def delete_session(request):
    # del request.session['name']
    request.session.flush()
    return render (request,'delete_session.html')