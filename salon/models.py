from django.db import models
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField

class Treatment(models.Model):
    appointment_type = models.CharField(max_length=150)
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=225)
    image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DecimalField(max_digits=3, decimal_places=0)
    display = models.BooleanField(default=False)

class Planning(models.Model):
    validate_times = RegexValidator(r'^(?:[01]\d|2[1-3]):[0-5]\d(?::[0-5]\d)?(?:,(?:[01]\d|2[1-3]):[0-5]\d(?::[0-5]\d)?)*$', 'Please enter comma seperated times, without spaces, like so: 12:00,13:15')
    validate_dates = RegexValidator(r'^(\s{0,})(\d{2}\.\d{2}\.\d{4})(,\d{2}\.\d{2}\.\d{4}){1,}(\s){0,}$', 'Please enter comma seperated dates (dd.mm.yyyy), without spaces, like so: 01.11.2028,02.11.2028')
    validate_weekdays = RegexValidator(r'^[0-6](,[0-6])*$', "Please enter valid numbers for weekdays, seperated by comma's. Values from 0-6, starting with sunday at value 0 (0,1,3 for example).")

    title = models.CharField(max_length=150, unique=True) 
    allow_times = models.TextField(default="", validators=[validate_times])
    disabled_dates = models.TextField(default="", validators=[validate_dates])
    disabled_weekdays = models.TextField(default="", validators=[validate_weekdays])