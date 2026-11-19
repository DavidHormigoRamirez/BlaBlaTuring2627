from django.urls import path
from .views import *

urlpatterns = [
    path("", BookingListView.as_view(), name="Booking-list"),
]