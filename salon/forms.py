from .models import Appointment
from django import forms

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('treatment_name', 'user', 'date_time')