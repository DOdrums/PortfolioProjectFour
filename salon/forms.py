from .models import Appointment
from django import forms

class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['treatment_name'].queryset = self.fields['treatment_name'].queryset.exclude(active=False)

    class Meta:
        model = Appointment
        
        fields = ('treatment_name', 'date_time', 'email', 'first_name', 'last_name', 'phone_number')
        labels = {
            'treatment_name': ('Treatment'), 'date_time':   ('Date')
        }
        # for fieldname, field in fields:
        #     field.widget.attrs.update({
        #     'class': 'custom-form-field'
        # })