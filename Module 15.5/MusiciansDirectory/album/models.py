from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from musician.models import musicianModel
# Create your models here.


class albumModel(models.Model):
    albumName=models.CharField(max_length=50)
    albumReleaseDate=models.DateField()
    rating=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    musician=models.ForeignKey(musicianModel,on_delete=models.CASCADE)

    def __str__(self):
        return self.albumName