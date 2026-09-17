from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Profile


class SignUpTests(TestCase):
    """Registering creates a User, a Profile with the chosen role, and signs them in."""

    def test_signup_page_loads(self):
        response = self.client.get(reverse("rota:signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_creates_user_and_profile(self):
        response = self.client.post(reverse("rota:signup"), {
            "username": "newcook",
            "email": "cook@example.com",
            "role": "cook",
            "password1": "Sturdy-Passphrase-42",
            "password2": "Sturdy-Passphrase-42",
        })

        self.assertRedirects(response, reverse("rota:home"))

        user = User.objects.get(username="newcook")
        self.assertEqual(user.profile.role, "cook")

    def test_mismatched_passwords_create_nothing(self):
        self.client.post(reverse("rota:signup"), {
            "username": "nope",
            "email": "nope@example.com",
            "role": "organiser",
            "password1": "Sturdy-Passphrase-42",
            "password2": "Different-Passphrase-43",
        })

        self.assertFalse(User.objects.filter(username="nope").exists())
        self.assertEqual(Profile.objects.count(), 0)


class LoginLogoutTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="organiser1",
            password="Sturdy-Passphrase-42",
        )
        Profile.objects.create(user=self.user, role="organiser")

    def test_login_works(self):
        logged_in = self.client.login(
            username="organiser1",
            password="Sturdy-Passphrase-42",
        )
        self.assertTrue(logged_in)

    def test_logout_requires_post(self):
        """Django 5 refuses a GET to the logout view."""
        self.client.login(username="organiser1", password="Sturdy-Passphrase-42")

        self.assertEqual(self.client.get(reverse("logout")).status_code, 405)
        self.assertEqual(self.client.post(reverse("logout")).status_code, 302)
