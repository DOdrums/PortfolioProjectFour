from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django import utils
class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.email = data["email"]
        user.phone_number = data['phone_number']
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        user.save()
        return user