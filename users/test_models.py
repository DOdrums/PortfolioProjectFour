from django.test import TestCase
from .models import User


class TestUserModel(TestCase):

    def setUp(self):
        User.objects.create(email="dirkornee@hotmail.com", first_name="Henk", last_name="Frits", phone_number="0611111111", password="lolololol")

    def test_create_user(self):
        user = User.objects.get(email="dirkornee@hotmail.com")
        email = user.email
        self.assertEqual(email, "dirkornee@hotmail.com")

    def test_delete_user(self):
        user = User.objects.get(email="dirkornee@hotmail.com")
        user.delete()
        self.assertFalse(User.objects.filter(email="dirkornee@hotmail.com").exists())
