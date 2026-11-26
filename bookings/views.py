# bookings/views.py
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Booking

class BookingListView(ListView):
    model = Booking

class BookingDetailView(DetailView):
    model = Booking
    template_name = "bookings/booking_detail.html"