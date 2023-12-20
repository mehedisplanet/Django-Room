from django.db import models

# Create your models here.

class Student(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    father_name=models.TextField(default=None)
    address=models.TextField(default="Bangladesh")

    def __str__(self):
        return f"{self.roll} - {self.name} - {self.address}"