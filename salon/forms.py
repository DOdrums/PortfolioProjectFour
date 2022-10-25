from .models import Appointment
from django import forms

class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['treatment_name'].queryset = self.fields['treatment_name'].queryset.exclude(active=False)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
            'class': 'custom-form-field'
        })


    class Meta:
        model = Appointment 
        fields = ('treatment_name', 'date_time', 'email', 'first_name', 'last_name', 'phone_number')
        labels = {
            'treatment_name': ('Treatment'), 'date_time':   ('Date'), 'email': ('Email*'), 'first_name': ('First name*'), 'last_name': ('Last name*')
        }