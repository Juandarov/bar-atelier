from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Services


class ServicesList(ListView):
    model = Services
    context_object_name = "services"