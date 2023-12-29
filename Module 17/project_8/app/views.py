from django.shortcuts import render, redirect
from .forms import RegisterForm, UserChange
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# Create your views here.


def home(request):
    return render(request, 'home.html')


def signUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, 'Account create successfully')
                form.save(commit=True)
                print(form.cleaned_data)
        else:
            form = RegisterForm()
        return render(request, './signUp.html', {'data': form})
    else:
        return redirect('profile')


def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=name, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'data': form})
    else:
        return redirect('profile')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'data': request.user})
    else:
        return redirect('login')
    


def userLogOut(request):
    logout(request)
    return redirect('login')


def passChange(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'passChange.html', {'data': form})
    else:
        return redirect('signUp')


def passChange2(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'passChange2.html', {'data': form})
    else:
        return redirect('signUp')


def userChange(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = UserChange(request.POST, instance=request.user)
            if form.is_valid():
                messages.success(request, 'Account updated successfully')
                form.save(commit=True)
                print(form.cleaned_data)
                return redirect('profile')
        else:
            form = UserChange(instance=request.user)
        return render(request, './userChange.html', {'data': form})
    else:
        return redirect('signUp')
