from django.shortcuts import render

# Create your views here.

from .models import User

from django.views.generic.list import ListView

def index(request):
    pass

class UserListView(ListView):
    model = User