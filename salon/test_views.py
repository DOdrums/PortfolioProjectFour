from django.test import TestCase
from .models import Treatment

class TestViews(TestCase):

    def test_get_home(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_about(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_get_gallary(self):
        response = self.client.get("/gallery")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')

    def test_get_contact(self):
        response = self.client.get("/contact")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_get_treatments(self):
        response = self.client.get("/treatments")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'treatments.html')
