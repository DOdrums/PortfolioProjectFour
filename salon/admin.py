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

class TreatmentInline(admin.StackedInline):
    model = Treatment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ['date_time']
    inlines = [TreatmentInline]


    # def get_treatment_title(self, obj):
    #     return obj.treatment.title

    # def get_treatment_duration(self, obj):
    #     return obj.treatment.duration
    
