from django.db import models

# Create your models here.

class categoryModel(models.Model):
    categoryName=models.CharField(max_length=50)

    def __str__(self):
        return self.categoryName
