from django.db import models


class ParkingZone(models.Model):
    zone_type = models.CharField(max_length=50)
    number_of_spaces = models.IntegerField()
    description = models.CharField(max_length=100)


class SpaceAvailability(models.Model):
    zone = models.ForeignKey(ParkingZone, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    free_spaces = models.IntegerField()