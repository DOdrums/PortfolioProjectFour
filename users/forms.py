from allauth.account.forms import SignupForm, LoginForm
from django import forms

from users.models import User

class CustomSignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(required=False)
        self.fields['last_name'] = forms.CharField(required=False)
        self.fields['phone_number'] = forms.CharField(required=False)

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

    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
            'class': 'custom-form-field'
        }) 

class EditUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        for fieldname, field in self.fields.items():
            field.widget.attrs.update({
            'class': 'custom-form-field'
        }) 
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number')