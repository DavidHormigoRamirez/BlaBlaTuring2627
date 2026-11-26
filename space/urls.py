from django.urls import path
from .views import ParkingZoneListView, SpaceAvailabilityListView

urlpatterns = [
    path('zones/', ParkingZoneListView.as_view(), name='parking-zone-list'),
    path('availability/', SpaceAvailabilityListView.as_view(), name='space-availability-list'),
]
