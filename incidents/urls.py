from django.urls import path
from .views import IncidentsListView
from .views import IncidentsDetailView

urlpatterns = [
    path('', IncidentsListView.as_view(),name='incident-list'),
    path('<int:pk>/', IncidentsDetailView.as_view(),name='incident-detail'),
]