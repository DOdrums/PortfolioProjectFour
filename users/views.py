from django.shortcuts import render
from django.views import View
from users.forms import EditUserForm
from salon.models import Appointment, Treatment

# Create your views here.
class Dashboard(View):

    def get(self, request):
        user_dict = {}
        if request.user.is_authenticated:
            user_dict = {'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'phone_number': request.user.phone_number}
        else:
            user_dict = {}
        
        user_form = EditUserForm(initial=user_dict)

        appointmentQueryset1 = Appointment.objects.filter(user__email=request.user.email).order_by("date_time").values()
        appointmentQueryset2 = Appointment.objects.filter(email=request.user.email).order_by("date_time").values()
        appointmentQueryset = list(appointmentQueryset1 | appointmentQueryset2)
        print(appointmentQueryset)
        for dict in appointmentQueryset:
            dict["date_time"] = dict["date_time"].strftime("%A %d %B %Y, %H:%M")
            dict["duration"] = int(Treatment.objects.get(id=dict['treatment_name_id']).duration)
            dict["treatment_name"] = Treatment.objects.get(id=dict['treatment_name_id']).title
        context = {"user_form": user_form, "appointments": appointmentQueryset}
        return render(request, "user_dashboard.html", context=context)