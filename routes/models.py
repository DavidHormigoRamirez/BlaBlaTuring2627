import datetime

from django.db import models

# Route model
# Represents a route defined by an user
class Route(models.Model):
    description = models.CharField(max_length=100)
    owner = models.ForeignKey('user.User',on_delete=models.CASCADE)
    active = models.BooleanField()
    # Dates wheen the route is valid
    from_date = models.DateField()
    to_date = models.DateField()
    departure_time = models.TimeField()
    leave_time = models.TimeField(default=datetime.time(hour=15,minute=45))
