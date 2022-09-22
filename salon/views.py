from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.list import ListView
from .models import Treatment


# Create your views here.
class HomePage(ListView):
    model = Treatment
    template_name = "index.html"

    def get_treatment_data(self):
        queryset = Treatment.objects.order_by('title')
        treatments = queryset.objects.values()
        return treatments