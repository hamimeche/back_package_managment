from django.contrib import admin

from items.models import Item


@admin.register(Item)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["label", "quantity", "package"]

