from django.db import models

# Create your models here.
class Vehicle(models.Model):
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    year_of_manufacture = models.IntegerField()
    make = models.CharField(max_length=50)
    imported = models.BooleanField(default=False)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.make} {self.model}" # Retorna por exemplo Toyota Corolla