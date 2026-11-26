from django.db import models

# Create your models here.
class Vehicle(models.Model):
    description = models.CharField(max_length=100)
    active = models.BooleanField()

    class Registration(models.TextChoices):
        number = models.CharField(max_length=10, unique=True)
        def __str__(self):
            return self.number