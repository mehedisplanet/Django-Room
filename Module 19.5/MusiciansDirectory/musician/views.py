from . import forms
from .forms import musicianForm
from .models import musicianModel
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.

@method_decorator(login_required, name='dispatch')
class AddMusician(CreateView):
    model = musicianModel
    form_class = musicianForm
    template_name = 'addMusician.html'
    success_url = reverse_lazy('addMusician')


@method_decorator(login_required, name='dispatch')
class EditMusician(UpdateView):
    model = musicianModel
    form_class = musicianForm
    template_name = 'addMusician.html'
    success_url = reverse_lazy('homepage')


class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self) -> str:
        return reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, 'Logged In SuccessFull')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Logged In Information Incorrect')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context


def user_logout(request):
    logout(request)
    return redirect('homepage')

# class UserLogoutView(View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('login')


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
