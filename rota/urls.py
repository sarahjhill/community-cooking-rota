from django.urls import path

from . import views

app_name = "rota"

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("rotas/new/", views.rota_create, name="rota_create"),
    path("rotas/<int:pk>/", views.rota_detail, name="rota_detail"),
    path("rotas/<int:pk>/edit/", views.rota_update, name="rota_update"),
    path("rotas/<int:pk>/delete/", views.rota_delete, name="rota_delete"),
]
