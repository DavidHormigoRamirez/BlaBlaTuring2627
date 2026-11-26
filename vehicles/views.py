from .models import Vehicle
from django.views.generic.list import ListView

# Create your views here.


class VehicleListView(ListView):
    model = Vehicle