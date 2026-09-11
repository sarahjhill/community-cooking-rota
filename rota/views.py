from django.shortcuts import render

from .models import Rota


def home(request):
    """Landing page: every rota, newest start date first (see Rota.Meta)."""
    return render(request, "rota/home.html", {"rotas": Rota.objects.all()})
