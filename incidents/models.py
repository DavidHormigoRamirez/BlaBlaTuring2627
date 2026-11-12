from django.db import models

# Create your models here.

class Incident(models.Model):
    subject = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    severity =