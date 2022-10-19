from time import strftime
from django.shortcuts import render
from django.views import View
from .forms import AppointmentForm
from .models import Appointment, Treatment, Planning
import json


# Create your views here.
class HomePage(View):

    def get(self, request):
        queryset = list(Treatment.objects.filter(display=True).order_by("title").values())
        treatments = {"treatments": queryset}
        return render(request, "index.html", context=treatments)

class BookingModule(View):

    def get(self, request):
        planningQueryset = list(Planning.objects.filter(active=True).order_by("title").values())
        appointmentQueryset = list(Appointment.objects.order_by("date_time").values())
        treatmentQueryset = list(Treatment.objects.filter(display=True).order_by("title").values())
        for dict in appointmentQueryset:
            dict["date_time"] = dict["date_time"].isoformat()
            dict["duration"] = int(treatmentQueryset[dict["treatment_name_id"] - 1]["duration"])
        context = {"planning": json.dumps(planningQueryset), "appointments": json.dumps(appointmentQueryset), "appointment_form": AppointmentForm}
        return render(request, "book.html", context=context)