from . import forms
from .forms import carForm
from .models import CarModel,Purchase
from . import models
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import CreateView,DetailView
from django.contrib import messages
from django.urls import reverse_lazy

# Create your views here.


class AddCar(CreateView):
    model=CarModel
    form_class=carForm
    template_name='register.html'
    success_url=reverse_lazy('register')


class DetailsPostView(DetailView):
    model = models.CarModel
    template_name = 'details.html'

    def post(self,request,*args,**kwargs):
        comment_form=forms.CommentForm(data=self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
        return self.get(request,*args,**kwargs)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comments_form'] = comment_form
        return context
    

@login_required
def purchase(request,id):
    car = CarModel.objects.get(id=id)
    if car.quantity > 0:
            car.quantity -= 1
            car.save()
            Purchase.objects.create(user=request.user, car=car)
            
            messages.success(request, "Buy successfully")
            return redirect('profile')
    else:
            messages.error(request, "Out Of Stock")
            return redirect('profile')