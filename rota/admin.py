from django.contrib import admin

from .models import Profile, Rota, Slot


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "created_at")
    list_filter = ("role",)


@admin.register(Rota)
class RotaAdmin(admin.ModelAdmin):
    list_display = ("recipient_name", "organiser", "start_date", "end_date")
    list_filter = ("organiser",)
    search_fields = ("recipient_name", "occasion")


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ("rota", "date", "cook", "claimed_at")
    list_filter = ("rota",)
