from django.urls import path
from . import views

urlpatterns = [
    path('zones/', views.zone_list, name='zone_list'),
    path('availability/', views.availability_list, name='availability_list'),
]