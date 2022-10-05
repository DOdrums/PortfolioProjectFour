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
    validate_times = RegexValidator(r'^(?:[01]\d|2[1-3]):[0-5]\d(?::[0-5]\d)?(?:,(?:[01]\d|2[1-3]):[0-5]\d(?::[0-5]\d)?)*$', 'Please enter comma seperated times, like so: 12:00, 13:15')
    allow_times = models.TextField(default="", validators=[validate_times])