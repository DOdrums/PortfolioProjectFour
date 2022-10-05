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
        queryset = list(Planning.objects.order_by("allow_times").values())
        plan_list = queryset[0]["allow_times"].split(",")
        planning = {"planning": json.dumps(plan_list)}
        return render(request, "book.html", context=planning)