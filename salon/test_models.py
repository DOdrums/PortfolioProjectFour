from datetime import datetime
from django.test import TestCase
from .models import Planning, Treatment, Appointment

class TestTreatmentModel(TestCase):

    def setUp(self):
        Treatment.objects.create(title="coolbeans", price=20, duration=100)

    def test_create_treatment(self):
        treatment = Treatment.objects.get(title="coolbeans")
        item_title = treatment.title
        self.assertEqual(item_title, "coolbeans")

    def test_delete_treatment(self):
        treatment = Treatment.objects.get(title="coolbeans")
        treatment.delete()
        self.assertFalse(Treatment.objects.filter(title="coolbeans").exists())

class TestAppointmentModel(TestCase):

    def setUp(self):
        date = datetime.today()
        Appointment.objects.create(email="dirkornee@hotmail.com", first_name="Henk", last_name="Frits", phone_number="0611111111", date_time = date)    

    def test_create_appointment(self):
        appointment = Appointment.objects.get(phone_number="0611111111")
        name = appointment.first_name
        self.assertEqual(name, "Henk")
   
    def test_delete_appointment(self):
        appointment = Appointment.objects.get(phone_number="0611111111")
        appointment.delete()
        self.assertFalse(Appointment.objects.filter(phone_number="0611111111").exists())
    
class TestPlanningModel(TestCase):

    def setUp(self):
        Planning.objects.create(title="planning", active="True", allow_times="10:00, 13:00, 14:15", disabled_weekdays="2,6", disabled_dates = "01.11.2028,02.11.2028")    

    def test_create_planning(self):
        planning = Planning.objects.get(title="planning")
        allow_times = planning.allow_times
        self.assertEqual(allow_times, "10:00, 13:00, 14:15") 
   
    def test_delete_planning(self):
        planning = Planning.objects.get(title="planning")
        planning.delete()
        self.assertFalse(Planning.objects.filter(title="planning").exists())
