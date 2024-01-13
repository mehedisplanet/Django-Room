from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
# Create your views here.


def signUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account Created Successfully')
                form.save()
        else:
            form = SignUpForm()
        return render(request, './signUp.html', {'data': form})
    else:
        return redirect('profile')


def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                messages.success(request, 'Account Logged In Successfully')
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=name, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, './login.html', {'data': form})
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'data': request.user})
    else:
        return redirect('login')


def logOut(request):
    logout(request)
    messages.warning(request, 'Account Logged Out Successfully')
    return redirect('homepage')

def passChange(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.warning(request, 'Password Change Successfully')
                return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,'passChange.html',{'data':form})
    else:
        return redirect('signUp')
    
def passChange2(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                messages.warning(request, 'Password Change Successfully')
                return redirect('profile')
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,'passChange2.html',{'data':form})
    else:
        return redirect('signUp')