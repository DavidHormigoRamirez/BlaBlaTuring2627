from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<html><head><title>Bookings Page</title></head><body><h1>Bookings page</h1></body></html>")