from django.urls import path
from config.urls import urlpatterns
from .views import VehicleListView, VehicleDetailView

urlpatterns = [
    path('', VehicleListView.as_view(), name='vehicle_list'),
    path('<int:pk>/', VehicleDetailView.as_view(),name='vehicle-detail'),
]