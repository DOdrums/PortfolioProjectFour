from django.db import models
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
