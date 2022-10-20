from .models import Appointment
from django import forms

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('treatment_name', 'date_time', 'email', 'first_name', 'last_name', 'phone_number')
    
        # for fieldname, field in fields:
        #     field.widget.attrs.update({
        #     'class': 'custom-form-field'
        # })