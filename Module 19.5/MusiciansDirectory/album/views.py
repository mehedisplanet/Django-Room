from django.shortcuts import render,redirect
from .forms import albumForm
from .models import albumModel
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.



@method_decorator(login_required, name='dispatch')
class AddAlbum(CreateView):
    model=albumModel
    form_class=albumForm
    template_name='addAlbum.html'
    success_url=reverse_lazy('addAlbum')


@method_decorator(login_required, name='dispatch')
class EditAlbum(UpdateView):
    model=albumModel
    form_class=albumForm
    template_name='addAlbum.html'
    success_url=reverse_lazy('homepage')


@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = albumModel
    template_name = 'delete.html'
    success_url = reverse_lazy('homepage')
