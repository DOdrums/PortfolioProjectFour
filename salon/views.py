from time import strftime
from datetime import datetime, timedelta
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import AppointmentForm, ContactForm
from .models import Appointment, Treatment, Planning, GalleryImage
import json

class HomePage(View):

    def get(self, request):
        queryset = list(Treatment.objects.filter(display=True).order_by("title").values())
        treatments = {"treatments": queryset, "is_home": True}
        return render(request, "index.html", context=treatments)

class BookingModule(View):

    def get(self, request):

        user_dict = {}
        if request.user.is_authenticated:
            user_dict = {'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name, 'phone_number': request.user.phone_number} 
        else:
            user_dict = {}

        yesterday = datetime.today() - timedelta(days=1)
        appointmentQueryset = list(Appointment.objects.filter(date_time__gt=yesterday).order_by("date_time").values())
        planningQueryset = list(Planning.objects.filter(active=True).order_by("title").values())

        for dict in appointmentQueryset:
            dict["date_time"] = dict["date_time"].isoformat()
            dict["duration"] = int(Treatment.objects.get(id=dict['treatment_name_id']).duration)

        form = AppointmentForm(initial=user_dict)
        context = {"planning": json.dumps(planningQueryset), "appointments": json.dumps(appointmentQueryset), "appointment_form": form}
        return render(request, "book.html", context=context)

    def post(self, request):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            subject = "Nailsbyfaar booking"
            if form.cleaned_data['phone_number']:
                phone = form.cleaned_data['phone_number']
            else:
                phone = "-"
            merge_data = {
                'treatment': form.cleaned_data['treatment_name'].title,
                'date': form.cleaned_data['date_time'].strftime("%A %d %B %Y, %H:%M"),
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'phone': phone,
            }
            html_body = render_to_string("email/email-book-inlined.html", context=merge_data)
            text_body = "\n".join(merge_data.values())
            form.save()
            try:
                msg = EmailMultiAlternatives(subject=subject, body=text_body, from_email='dirkornee@hotmail.com', to=['dirkrnee@icloud.com'])
                msg.attach_alternative(html_body, "text/html")
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect("thankyou")
        else:
            form = AppointmentForm()
            return HttpResponseRedirect("book-error")

class ThankYou(View):

    def get(self, request):
        return render(request, "booked.html")

class BookError(View):

    def get(self, request):
        return render(request, "book-error.html")

class Treatments(View):

    def get(self, request):
        queryset = list(Treatment.objects.filter(display=True).order_by("title").values())
        treatments = {"treatments": queryset}
        return render(request, "treatments.html", context=treatments)

class About(View):

    def get(self, request):
        return render(request, "about.html")

class Gallery(View):

    def get(self, request):
        queryset = list(GalleryImage.objects.filter(active=True).order_by("name").values())
        images = {"images": queryset}
        return render(request, "gallery.html", context=images)

class Contact(View):

    def get(self, request):
        user_dict = {}
        if request.user.is_authenticated:
            user_dict = {'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name}
        else:
            user_dict = {}
        form = ContactForm(initial=user_dict)
        context = {"contact_form": form}
        return render(request, "contact.html", context=context)

    def post(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = "Nailsbyfaar website question"
                body = {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'email': form.cleaned_data['email'],
                    'subject': form.cleaned_data['subject'],
                    'message': form.cleaned_data['message'],
                }
                message = "\n".join(body.values())

                try:
                    send_mail(subject, message, 'dirkornee@hotmail.com', ['dirkrnee@icloud.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('contact')
