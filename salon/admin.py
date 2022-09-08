from django.contrib import admin
from .models import Treatment

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):

    list_display = ('title', 'appointment_type')
    list_filter = ('appointment_type', 'price')
    search_fields = ['title', 'description', 'appointment_type']