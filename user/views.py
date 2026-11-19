from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import User
from django.views.generic.list import ListView
# Create your views here.



def index(request):
    pass

class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'