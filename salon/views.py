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
        plan_list = queryset[0]["allow_times"].split(",")
        d_dates = queryset[0]["disabled_days"].split(",")
        planning = {"times": json.dumps(plan_list), "d_dates": json.dumps(d_dates)}
        return render(request, "book.html", context=planning)