from django.shortcuts import render
from carModel.models import CarModel
from carBrand.models import carBrand


def home(request, category_slug=None):
    data = CarModel.objects.all()
    if category_slug is not None:
        category = carBrand.objects.get(slug=category_slug)
        data = CarModel.objects.filter(carBrandName=category)
    categories = carBrand.objects.all()
    return render(request, 'home.html', {'data': data, 'data_2': categories})
