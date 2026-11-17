from .models import Route
from django.views.generic.list import ListView


# Create your views here.
def index(request):
    pass

class RoutesListView(ListView):
    model = Route