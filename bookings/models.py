from django.db import models

# Create your models here.
class Booking(models.Model):

    ReserveHour = models.DateTimeField()
    active = models.BooleanField(default=True)
    #Relacion user
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    #Relacion routes
    route = models.ForeignKey('routes.Route', on_delete=models.CASCADE)
