from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from carModel.models import Purchase
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('homepage')
    
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : register_form, 'type' : 'Register'})


class UserLoginView(LoginView):
    template_name='register.html'

    def get_success_url(self) -> str:
        return reverse_lazy('homepage')
    
    def form_valid(self,form):
        messages.success(self.request,'Logged In SuccessFull')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.success(self.request,'Logged In Information Incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['type']='Login'
        return context


@login_required
def profile(request):
    user = Purchase.objects.filter(user=request.user)
    data = [purchase.car for purchase in user]
    return render(request, 'profile.html', {'data': data})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})


class UserLogoutView(LogoutView):
    def get_success_url(self):
        messages.success(self.request, "Logout successfully")
        return reverse_lazy('homepage')
    

def user_logout(request):
    logout(request)
    return redirect('homepage')
