from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import SignUpForm
from .models import Profile, Rota


def home(request):
    """Landing page: every rota, newest start date first."""
    return render(request, "rota/home.html", {"rotas": Rota.objects.all()})


def signup(request):
    """Create a User, attach a Profile with their chosen role, sign them in."""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, role=form.cleaned_data["role"])
            login(request, user)
            messages.success(
                request,
                f"Welcome, {user.username}. Your account is ready.",
            )
            return redirect("rota:home")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})