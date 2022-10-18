from datetime import timedelta
from django.contrib import admin
from .models import Treatment, Planning, Appointment

@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):

    list_display = ('title', 'appointment_type')
    list_filter = ('appointment_type', 'price')
    search_fields = ['title', 'description', 'appointment_type']

@admin.register(Planning)
class PlanningAdmin(admin.ModelAdmin):

    list_display = ['title']

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ['date_time', 'get_end_time', 'get_treatment_duration', 'get_treatment_title']
    ordering = ['-date_time']

    @admin.display(description="Treatment")
    def get_treatment_title(self, obj):
        return obj.treatment_name.title

    @admin.display(description="Duration")
    def get_treatment_duration(self, obj):
        return obj.treatment_name.duration

    @admin.display(description="End Time")
    def get_end_time(self, obj):
        start_time = obj.date_time
        duration = int(obj.treatment_name.duration)
        end_time = start_time + timedelta(minutes=duration)
        return end_time
