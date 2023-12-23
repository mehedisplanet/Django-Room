from django.db import models

# Create your models here.


class MyModel(models.Model):
    name=models.CharField(max_length=25)
    auto_field = models.AutoField(primary_key=True)
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    email_field = models.EmailField()
    float_field = models.FloatField()
    big_integer_field = models.BigIntegerField()
    date_field = models.DateField()
    duration_field = models.DurationField()


    def __str__(self):
        return f"{self.name}"
