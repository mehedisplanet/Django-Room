from django.db import models
from django.contrib.auth.models import User
from carBrand.models import carBrand

# Create your models here.


class CarModel(models.Model):
    image=models.ImageField(upload_to='carModel/media/uploads/',blank=True,null=True)
    carName=models.CharField(max_length=50)
    carPrice=models.IntegerField()
    carBrandName=models.ForeignKey(carBrand,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    description=models.TextField(default='This car')

    def __str__(self):
        return self.carName
    


class Comment(models.Model):
    post=models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comments by {self.name}'
    

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)