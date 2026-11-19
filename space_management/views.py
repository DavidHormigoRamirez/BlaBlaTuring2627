from django.shortcuts import render
from .models import ParkingZone
from .models import SpaceAvailability


def zone_list(request):
    zones = ParkingZone.objects.all()
    return render(request, 'space_management/zone_list.html', {
        'zones': zones
    })

def availability_list(request):
    availability = SpaceAvailability.objects.all()
    return render(request, 'space_management/availability_list.html', {
        'availability': availability
    })
