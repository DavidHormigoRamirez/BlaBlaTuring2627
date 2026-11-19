from django.urls import path
from .views import *

urlpatterns = [
    # bookings/urls.py
    path("", BookingListView.as_view(), name="Booking-list"),
    path("<int:pk>/", BookingDetailView.as_view(), name="Booking-detail"),
]