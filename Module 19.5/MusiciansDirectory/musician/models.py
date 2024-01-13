from django.db import models

# Create your models here.

class musicianModel(models.Model):
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    email=models.EmailField()
    phoneNumber=models.CharField(max_length=15)
    instrumentType=models.CharField(max_length=30)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"