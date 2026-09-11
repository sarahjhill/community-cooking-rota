from django.urls import path

from . import views

app_name = "rota"

urlpatterns = [
    path("", views.home, name="home"),
]
