from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from users.forms import EditUserForm
from users.forms import EditAppointmentForm
from salon.models import Appointment, Treatment, Planning
from users.models import User
import json

class Dashboard(View):

    def get(self, request):
        user_dict = {}
        if request.user.is_authenticated:
            user_dict = {'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'phone_number': request.user.phone_number}
        else:
           return HttpResponseRedirect(reverse("account_login")) 
        
        user_form = EditUserForm(initial=user_dict)

        yesterday = datetime.today() - timedelta(days=1)

        appointmentQueryset1 = Appointment.objects.filter(date_time__gt=yesterday).filter(user__email=request.user.email).order_by("date_time").values()
        appointmentQueryset2 = Appointment.objects.filter(date_time__gt=yesterday).filter(email=request.user.email).order_by("date_time").values()
        appointmentQueryset = list(appointmentQueryset1 | appointmentQueryset2)
        for dict in appointmentQueryset:
            date = dict["date_time"]
            check_date = datetime.now() + timedelta(days=2)
 
            if date <= check_date:
                dict["not_cancellable"] = True
                print("don't cancel me")
            dict["date_time_short"] = dict["date_time"].strftime("%A %d %B, %H:%M")
            dict["date_time"] = dict["date_time"].strftime("%A %d %B %Y, %H:%M")
            dict["duration"] = int(Treatment.objects.get(id=dict['treatment_name_id']).duration)
            dict["treatment_name"] = Treatment.objects.get(id=dict['treatment_name_id']).title
        context = {"user_form": user_form, "appointments": appointmentQueryset}
        return render(request, "user-dashboard.html", context=context)
    
    def post(self, request):

        yesterday = datetime.today() - timedelta(days=1)

        appointmentQueryset1 = Appointment.objects.filter(date_time__gt=yesterday).filter(user__email=request.user.email).order_by("date_time").values()
        appointmentQueryset2 = Appointment.objects.filter(date_time__gt=yesterday).filter(email=request.user.email).order_by("date_time").values()
        appointmentQueryset = list(appointmentQueryset1 | appointmentQueryset2)
        for dict in appointmentQueryset:
            dict["date_time_short"] = dict["date_time"].strftime("%A %d %B, %H:%M")
            dict["date_time"] = dict["date_time"].strftime("%A %d %B %Y, %H:%M")
            dict["duration"] = int(Treatment.objects.get(id=dict['treatment_name_id']).duration)
            dict["treatment_name"] = Treatment.objects.get(id=dict['treatment_name_id']).title
        
        if request.POST.get('appointment_id', default=None):
            appointment_id = request.POST.get('appointment_id')
            appointment = Appointment.objects.filter(id=appointment_id)
            if request.user.email == Appointment.objects.get(id=appointment_id).email:
                appointment.delete()
                return HttpResponseRedirect("dashboard")
            else:
                return HttpResponseRedirect("dashboard")
            

        if request.POST.get('first_name', default=None):
            form = EditUserForm(data=request.POST, instance=request.user)
            if form.is_valid():
                user = form.save(commit=False)
                user.save(update_fields=['first_name', 'last_name', 'phone_number'])

                user_dict = {}
                if request.user.is_authenticated:
                    user_dict = {'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'phone_number': request.user.phone_number}
                else:
                    user_dict = {}
                
                user_form = EditUserForm(initial=user_dict)

                context = {"user_form": user_form, "appointments": appointmentQueryset, "saved": True}
                return render(request, "user-dashboard.html", context=context)
            else:
                user_dict = {'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'phone_number': request.user.phone_number}
                user_form = EditUserForm(initial=user_dict)

                context = {"user_form": user_form, "appointments": appointmentQueryset, "not_saved": True}
                return render(request, "user-dashboard.html", context=context)

class EditAppointment(View):

    def get(self, request, slug):
        if request.user.email == Appointment.objects.get(id=slug).email: 
            treatment_id = Appointment.objects.get(id=slug).treatment_name
            appointment_date = Appointment.objects.get(id=slug).date_time
            appointment_date = appointment_date.strftime("%d-%m-%Y %H:%M")
            print(appointment_date)
            user_dict = {}
            treatments = Treatment.objects.filter(title=treatment_id).order_by("title").values()
            treatments_tuple = [(str(i["id"]) + "," + str(i["duration"]), i["title"] + " - " + str(i["duration"]) + " min - €" + str(i["price"])) for i in treatments]
            user_dict = {'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'phone_number': request.user.phone_number, 'date_time': appointment_date} 

            yesterday = datetime.today() - timedelta(days=1)
            appointmentQueryset = list(Appointment.objects.filter(date_time__gt=yesterday).order_by("date_time").values())
            planningQueryset = list(Planning.objects.filter(active=True).order_by("title").values())

            for dict in appointmentQueryset:
                dict["date_time"] = dict["date_time"].isoformat()
                dict["duration"] = int(Treatment.objects.get(id=dict['treatment_name_id']).duration)

            form = EditAppointmentForm(initial=user_dict)
            form.fields["treatment_name"].choices = treatments_tuple
            context = {"planning": json.dumps(planningQueryset), "appointments": json.dumps(appointmentQueryset), "appointment_form": form}
            return render(request, "edit-appointment.html", context=context)
        else:
            return render(request, "book-error.html")
        
    def post(self, request, slug):
        form = EditAppointmentForm(request.POST, instance=Appointment.objects.get(id=slug))
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            print(form.errors)
            form = EditAppointmentForm()
            return HttpResponseRedirect("book-error")