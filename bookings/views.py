from django.shortcuts import render
from .models import *
from django.views.generic.list import ListView


# Create your views here.
def index(request):
    pass

class BookingListView(ListView):
    model = Booking
