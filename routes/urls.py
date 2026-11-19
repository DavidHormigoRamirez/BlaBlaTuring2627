
from django.urls import path
from .views import RoutesListView

urlpatterns = [
        path('', RoutesListView.as_view(),name="route-list"),
    ]