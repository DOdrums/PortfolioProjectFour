from time import strftime
from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import AppointmentForm
from .models import Appointment, Treatment, Planning
import json


# Create your views here.
class HomePage(View):

    def get(self, request):
        queryset = list(Treatment.objects.filter(display=True).order_by("title").values())
        treatments = {"treatments": queryset, "is_home": True}
        return render(request, "index.html", context=treatments)

class BookingModule(View):

    def get(self, request):

        user_dict = {}
        if request.user.is_authenticated:
            user_dict = {'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'phone_number': request.user.phone_number} 
        else:
            user_dict = {}

        yesterday = datetime.today() - timedelta(days=1)
        appointmentQueryset = list(Appointment.objects.filter(date_time__gt=yesterday).order_by("date_time").values())
        planningQueryset = list(Planning.objects.filter(active=True).order_by("title").values())

        for dict in appointmentQueryset:
            dict["date_time"] = dict["date_time"].isoformat()
            dict["duration"] = int(Treatment.objects.get(id=dict['treatment_name_id']).duration)

        form = AppointmentForm(initial=user_dict)
        context = {"planning": json.dumps(planningQueryset), "appointments": json.dumps(appointmentQueryset), "appointment_form": form}
        return render(request, "book.html", context=context)

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thankyou")
        else:
            form = AppointmentForm()
            return HttpResponseRedirect("book-error")

class ThankYou(View):

    def get(self, request):
        return render(request, "booked.html")

class BookError(View):

    def get(self, request):
        return render(request, "book-error.html")

class Treatments(View):

    def get(self, request):
        queryset = list(Treatment.objects.filter(display=True).order_by("title").values())
        treatments = {"treatments": queryset}
        return render(request, "treatments.html", context=treatments)