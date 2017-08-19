from django.shortcuts import render
from django.views.generic import ListView
from .models import Object

class Main(ListView):
    template_name = 'main.html'
    model = Object