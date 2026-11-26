from django.views.generic.list import ListView
from .models import ParkingZone, SpaceAvailability


class ParkingZoneListView(ListView):
    model = ParkingZone


class SpaceAvailabilityListView(ListView):
    model = SpaceAvailability