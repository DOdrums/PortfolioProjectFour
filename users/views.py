from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from users.forms import EditUserForm
from salon.models import Appointment, Treatment
from users.models import User

# Create your views here.
class Dashboard(View):

    def get(self, request):
        user_dict = {}
        if request.user.is_authenticated:
            user_dict = {'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'phone_number': request.user.phone_number}
        else:
            user_dict = {}
        
        user_form = EditUserForm(initial=user_dict)

        yesterday = datetime.today() - timedelta(days=1)

        appointmentQueryset1 = Appointment.objects.filter(date_time__gt=yesterday).filter(user__email=request.user.email).order_by("date_time").values()
        appointmentQueryset2 = Appointment.objects.filter(date_time__gt=yesterday).filter(email=request.user.email).order_by("date_time").values()
        appointmentQueryset = list(appointmentQueryset1 | appointmentQueryset2)
        for dict in appointmentQueryset:
            dict["date_time_short"] = dict["date_time"].strftime("%A %d %B, %H:%M")
            dict["date_time"] = dict["date_time"].strftime("%A %d %B %Y, %H:%M")
            dict["duration"] = int(Treatment.objects.get(id=dict['treatment_name_id']).duration)
            dict["treatment_name"] = Treatment.objects.get(id=dict['treatment_name_id']).title
        context = {"user_form": user_form, "appointments": appointmentQueryset}
        return render(request, "user_dashboard.html", context=context)
    
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
                return render(request, "user_dashboard.html", context=context)
            else:
                user_dict = {'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'phone_number': request.user.phone_number}
                user_form = EditUserForm(initial=user_dict)

                context = {"user_form": user_form, "appointments": appointmentQueryset, "not_saved": True}
                return render(request, "user_dashboard.html", context=context)