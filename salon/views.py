from django.shortcuts import render
from django.views import View
from .models import Treatment, Planning
import json


# Create your views here.
class HomePage(View):

    def get(self, request):
        queryset = list(Treatment.objects.filter(display=True).order_by("title").values())
        treatments = {"treatments": queryset}
        return render(request, "index.html", context=treatments)

class BookingModule(View):

    def get(self, request):
        queryset = list(Planning.objects.order_by("title").values())
        planning = {"planning": json.dumps(queryset)}
        return render(request, "book.html", context=planning)