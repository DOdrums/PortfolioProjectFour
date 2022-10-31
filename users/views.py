from django.shortcuts import render
from django.views import View

# Create your views here.
class Dashboard(View):

    def get(self, request):
        user_data = {}
        user_appointments = {"user": user_data}
        return render(request, "user_dashboard.html", context=user_appointments)