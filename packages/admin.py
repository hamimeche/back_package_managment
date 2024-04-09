from django.contrib import admin

from packages.models import Package


@admin.register(Package)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["code", "weight", "delivery_date", "status"]

