"""URL configuration for the Community Cooking Rota project."""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("rota.urls")),
]
