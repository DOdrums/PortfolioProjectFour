from django.shortcuts import render
from django.views import View
from .models import Treatment


# Create your views here.
class HomePage(View):

    def get(self, request):
        # queryset = Treatment.objects.order_by("title").values()
        treatments = {"treat": "hello", "lol": "bananananaan", "soup": "jaaaaa"}
        return render(request, "index.html", context=treatments)
