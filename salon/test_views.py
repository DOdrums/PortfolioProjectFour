from django.test import TestCase
from .models import Treatment

class TestViews(TestCase):

    def test_get_treatments(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
