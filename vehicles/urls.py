from django.urls import path
from config.urls import urlpatterns
from .views import VehicleListView

urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle_list'),
]