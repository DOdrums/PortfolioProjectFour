from datetime import datetime, timedelta
import json
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import AppointmentForm, ContactForm
from .models import Appointment, Treatment, Planning, GalleryImage

class HomePage(View):
    """
    View to render homepage.
    """
    def get(self, request):
        """
        gets all the treatments from database and returns them as context.
        """
        queryset = list(Treatment.objects.filter(display=True).order_by("title").values())
        treatments = {"treatments": queryset, "is_home": True}
        return render(request, "index.html", context=treatments)

class BookingModule(View):
    """
    View to render the booking page and data.
    """

    def get(self, request):
        """
        Gets all neccesary data: Appointments, Treatments and Planning.
        Passes it as context while rendering book.html.
        """
        user_dict = {}
        if request.user.is_authenticated:
            user_dict = {
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'phone_number': request.user.phone_number}
        else:
            user_dict = {}

        yesterday = datetime.today() - timedelta(days=1)
        appointmentQueryset = list(Appointment.objects.filter(
            date_time__gt=yesterday).order_by("date_time").values())
        planningQueryset = list(Planning.objects.filter(active=True).order_by("title").values())

        for dict in appointmentQueryset:
            dict["date_time"] = dict["date_time"].isoformat()
            dict["duration"] = int(Treatment.objects.get(id=dict['treatment_name_id']).duration)

        form = AppointmentForm(initial=user_dict)
        context = {
            "planning": json.dumps(planningQueryset),
            "appointments": json.dumps(appointmentQueryset),
            "appointment_form": form}
        return render(request, "book.html", context=context)

    def post(self, request):
        """
        Post methode for booking an appointment.
        Checks if forms is valid and takes appropiate action.
        """
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
                msg = EmailMultiAlternatives(
                    subject=subject,
                    body=text_body,
                    from_email='dirkrnee@icloud.com',
                    to=[form.cleaned_data['email']]
                    )
                msg.attach_alternative(html_body, "text/html")
                msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect("thankyou")
        else:
            form = AppointmentForm()
            return HttpResponseRedirect("book-error")

class ThankYou(View):
    """
    Simple view to render the booked.html page for succesful bookings.
    """

    def get(self, request):
        """
        Get method, renders booked.html.
        """
        return render(request, "booked.html")

class BookError(View):
    """
    View to render page in case of unsuccesful booking.
    """

    def get(self, request):
        """
        Get method for rendering book-error html.
        """
        return render(request, "book-error.html")

class Treatments(View):
    """
    View to render treatments page.
    """

    def get(self, request):
        """
        Get method, taking treatments from database with 'display' set to true.
        """
        queryset = list(Treatment.objects.filter(display=True).order_by("title").values())
        treatments = {"treatments": queryset}
        return render(request, "treatments.html", context=treatments)

class About(View):
    """
    View to render about page.
    """

    def get(self, request):
        """
        Get method, to render about html.
        """
        return render(request, "about.html")

class Gallery(View):
    """
    View to render Gallery page.
    """

    def get(self, request):
        """
        Get method, taking all images set to active from database and
        render them in gallery html.
        """
        queryset = list(GalleryImage.objects.filter(active=True).order_by("name").values())
        images = {"images": queryset}
        return render(request, "gallery.html", context=images)

class Contact(View):
    """
    View to render contact page.
    """

    def get(self, request):
        """
        Gets user data if logged in and renders contact form with initial data.
        """
        user_dict = {}
        if request.user.is_authenticated:
            user_dict = {
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name}
        else:
            user_dict = {}
        form = ContactForm(initial=user_dict)
        context = {"contact_form": form}
        return render(request, "contact.html", context=context)

    def post(self, request):
        """
        Posts the contact form, by sending it as an email
        """
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                subject = "Nailsbyfaar website question"
                merge_data = {
                    'first_name': form.cleaned_data['first_name'],
                    'last_name': form.cleaned_data['last_name'],
                    'email': form.cleaned_data['email'],
                    'subject': form.cleaned_data['subject'],
                    'message': form.cleaned_data['message'],
                }
                html_body = render_to_string(
                    "email/email-contact-inlined.html", context=merge_data
                    )
                text_body = "\n".join(merge_data.values())
                try:
                    msg = EmailMultiAlternatives(
                        subject=subject,
                        body=text_body,
                        from_email='dirkrnee@icloud.com',
                        to=[form.cleaned_data['email']])
                    msg.attach_alternative(html_body, "text/html")
                    msg.send()
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('contact')
