from django.db import models
from category.models import categoryModel

# Create your models here.

class taskModel(models.Model):
    taskTitle=models.CharField(max_length=50)
    taskDescription=models.TextField()
    isCompleted=models.BooleanField(default=False)
    taskAssignDate=models.DateField()
    category=models.ManyToManyField(categoryModel)

    def __str__(self):
        return self.taskTitle