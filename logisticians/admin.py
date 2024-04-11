from django.contrib import admin

from logisticians.models import Logistician


@admin.register(Logistician)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["last_name", "first_name", "email"]
