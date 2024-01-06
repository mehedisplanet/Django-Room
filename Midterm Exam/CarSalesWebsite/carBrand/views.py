from . import forms
from .forms import carBrandForm
from .models import carBrand
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.


class AddBrand(CreateView):
    model=carBrand
    form_class=carBrandForm
    template_name='register.html'
    success_url=reverse_lazy('register')