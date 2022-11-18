from django.test import TestCase
from django.urls import reverse
from .models import User 

class TestViews(TestCase):

    def setUp(self):
        self.custom_user = User.objects.create_user(email="dirkornee@hotmail.com", first_name="Henk", last_name="Frits", phone_number="0611111111", password="lolololol")

    def test_get_dashboard(self):
        login = self.client.login(email="dirkornee@hotmail.com", password="lolololol")
        self.assertTrue(login)
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-dashboard.html')

    def test_get_dashboard_logged_out(self):
        login = self.client.login(email="dirkornee@hotmail.com", password="lolololol")
        self.assertTrue(login)
        logout = self.client.logout()
        response = self.client.get(reverse("dashboard"))
        # check redirect to login page.
        self.assertEqual(response.status_code, 302)

