from datetime import datetime
from .models import Appointment, Treatment
from django import forms

class AppointmentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        treatments = Treatment.objects.filter(active=True).order_by("title").values()
        treatments_tuples = [("", "---------------")]
        treatments_tuples = treatments_tuples + [(str(i["id"]) + "," + str(i["duration"]), i["title"] + " - " + str(i["duration"]) + " min - €" + str(i["price"])) for i in treatments]
        self.fields['treatment_name'] = forms.ChoiceField(choices=treatments_tuples)
        self.fields['date_time'] = forms.CharField()
        self.fields['date_time'].label = "Date"
        self.fields['date_time'].required = True 
        self.fields['email'].required = True 
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True 
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
            'class': 'custom-form-field'
        })

    class Meta:
        model = Appointment
        fields = ('treatment_name', 'date_time', 'email', 'first_name', 'last_name', 'phone_number')
        labels = {
            'treatment_name': ('Treatment')
        }

    def clean(self):
        cleaned_data = super().clean()
        treatment_value = cleaned_data["treatment_name"].split(",")
        treatment_id = int(treatment_value[0])
        treatment_name = Treatment.objects.get(id=treatment_id)
        cleaned_data["treatment_name"] = treatment_name
        print(cleaned_data)
        cleaned_data["date_time"] = datetime.strptime(cleaned_data["date_time"], '%d-%m-%Y %H:%M')
        return cleaned_data
        