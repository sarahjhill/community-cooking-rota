
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RotaForm, SignUpForm
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

def _require_organiser(request):
    """Stop the request here unless the signed-in user is an Organiser."""
    if not hasattr(request.user, "profile") or request.user.profile.role != "organiser":
        raise PermissionDenied("Only Organisers can do that.")


def rota_detail(request, pk):
    """Anyone can view a rota's dates — Cooks need this to see what's open."""
    rota = get_object_or_404(Rota, pk=pk)
    return render(request, "rota/rota_detail.html", {"rota": rota})


@login_required
def rota_create(request):
    _require_organiser(request)

    if request.method == "POST":
        form = RotaForm(request.POST)
        if form.is_valid():
            rota = form.save(commit=False)
            rota.organiser = request.user
            rota.save()
            messages.success(request, f"Rota for {rota.recipient_name} created.")
            return redirect("rota:rota_detail", pk=rota.pk)
    else:
        form = RotaForm()

    return render(request, "rota/rota_form.html", {"form": form, "heading": "New rota"})


@login_required
def rota_update(request, pk):
    rota = get_object_or_404(Rota, pk=pk)
    if rota.organiser != request.user:
        raise PermissionDenied("You can only edit your own rotas.")

    if request.method == "POST":
        form = RotaForm(request.POST, instance=rota)
        if form.is_valid():
            form.save()
            messages.success(request, "Rota updated.")
            return redirect("rota:rota_detail", pk=rota.pk)
    else:
        form = RotaForm(instance=rota)

    return render(request, "rota/rota_form.html", {"form": form, "heading": "Edit rota"})


@login_required
def rota_delete(request, pk):
    rota = get_object_or_404(Rota, pk=pk)
    if rota.organiser != request.user:
        raise PermissionDenied("You can only delete your own rotas.")

    if request.method == "POST":
        rota.delete()
        messages.success(request, "Rota deleted.")
        return redirect("rota:home")

    return render(request, "rota/rota_confirm_delete.html", {"rota": rota})