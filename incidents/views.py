from django.shortcuts import render
from .models import Incident
from django.views.generic.list import ListView
# Create your views here.

def index(request):
    pass

class IncidentsListView(ListView):
    model = Incident

class IncidentsDetailView(DetailView):
    model = Incident
    template_name = "Incidents/incidentDetail_list.html"