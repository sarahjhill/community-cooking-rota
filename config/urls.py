"""URL configuration for the Cook Book project."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("rota.urls")),
]
