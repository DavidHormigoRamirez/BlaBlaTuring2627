from django.shortcuts import render
from django.views.generic import DetailView
from .models import Vehicle
from django.views.generic.list import ListView

# Create your views here.

class VehicleListView(ListView):
    model = Vehicle

class VehicleDetailView(DetailView):
    model = Vehicle