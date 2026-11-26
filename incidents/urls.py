from django.urls import path
from .views import IncidentsListView

urlpatterns = [
    path('', IncidentsListView.as_view(),name='incident-list'),
]