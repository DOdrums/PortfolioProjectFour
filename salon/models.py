from django.db import models
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField
from users.models import User


class Treatment(models.Model):
    appointment_type = models.CharField(max_length=150)
    title = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    short_description = models.CharField(max_length=225)
    image = CloudinaryField('image', default='placeholder')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DecimalField(max_digits=3, decimal_places=0)
    display = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        #  Returns a string of title of treatment
        return f"{self.title}"

class Appointment(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.PROTECT, null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    treatment_name = models.ForeignKey(Treatment, related_name="treatment_name", on_delete=models.PROTECT, null=True)
    date_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        self.date_time = self.date_time.replace(tzinfo=None)
        super(Appointment, self).save(*args, **kwargs)

class Planning(models.Model):
    validate_times = RegexValidator(r'^(?:[01]\d|2[1-3]):[0-5]\d(?::[0-5]\d)?(?:,(?:[01]\d|2[1-3]):[0-5]\d(?::[0-5]\d)?)*$', 'Please enter comma seperated times, without spaces, like so: 12:00,13:15')
    validate_dates = RegexValidator(r'^(\s{0,})(\d{2}\.\d{2}\.\d{4})(,\d{2}\.\d{2}\.\d{4}){1,}(\s){0,}$', 'Please enter comma seperated dates (dd.mm.yyyy), without spaces, like so: 01.11.2028,02.11.2028')
    validate_weekdays = RegexValidator(r'^[0-6](,[0-6])*$', "Please enter valid numbers for weekdays, seperated by comma's. Values from 0-6, starting with sunday at value 0 (0,1,3 for example).")

    title = models.CharField(max_length=150, unique=True)
    allow_times = models.TextField(default="", validators=[validate_times])
    disabled_dates = models.TextField(default="", validators=[validate_dates])
    disabled_weekdays = models.TextField(default="", validators=[validate_weekdays])
    active = models.BooleanField(default=False)
