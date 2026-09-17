from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Profile


class SignUpForm(UserCreationForm):
    """Django's normal signup form, plus the Organiser/Cook choice."""

    email = forms.EmailField(
        required=True,
        help_text="We use this to send you rota updates.",
    )
    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES,
        widget=forms.RadioSelect,
        label="I am signing up as",
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    # Show the fields in a sensible order rather than Django's default.
    field_order = ["username", "email", "role", "password1", "password2"]