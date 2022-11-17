from datetime import datetime
from allauth.account.forms import SignupForm, LoginForm
from django import forms
from salon.models import Appointment, Treatment

from users.models import User

class CustomSignUpForm(SignupForm):
    """
    Form for signing up new users.
    """

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(required=False)
        self.fields['last_name'] = forms.CharField(required=False)
        self.fields['phone_number'] = forms.CharField(required=False)
        self.fields['phone_number'].label = "Phone number (optional)"
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
            'class': 'custom-form-field'
        })

    def save(self, request):
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        phone_number = self.cleaned_data['phone_number']


        user = super(CustomSignUpForm, self).save(request)
        return user


class CustomLoginForm(LoginForm):
    """
    Form for logging in.
    """

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
            'class': 'custom-form-field'
        })

class EditUserForm(forms.ModelForm):
    """
    Form for editting user data.
    """

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
            'class': 'custom-form-field'
        })

    class Meta:
        """
        Class to display fields with proper labels.
        """
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number')

class EditAppointmentForm(forms.ModelForm):
    """
    Form to edit appointment.
    """
    def __init__(self, *args, **kwargs):
        super(EditAppointmentForm, self).__init__(*args, **kwargs)
        treatments = Treatment.objects.filter(active=True).order_by("title").values()
        treatments_tuples = [("", "---------------")]
        treatments_tuples = treatments_tuples + [(str(
            i["id"]) + "," + str(
                i["duration"]), i["title"] + " - " + str(
                    i["duration"]) + " min - €" + str(i["price"])) for i in treatments]
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
        """
        Class to display fields with proper labels.
        """
        model = Appointment
        fields = (
            'treatment_name',
            'date_time',
            'email',
            'first_name',
            'last_name',
            'phone_number'
            )
        labels = {
            'treatment_name': ('Treatment')
        }

    def clean(self):
        cleaned_data = super().clean()
        treatment_value = cleaned_data["treatment_name"].split(",")
        treatment_id = int(treatment_value[0])
        treatment_name = Treatment.objects.get(id=treatment_id)
        cleaned_data["treatment_name"] = treatment_name
        cleaned_data["date_time"] = datetime.strptime(cleaned_data["date_time"], '%d-%m-%Y %H:%M')
        return cleaned_data
