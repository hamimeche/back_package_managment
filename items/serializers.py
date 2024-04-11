from rest_framework import serializers

from core.common import EagerLoadingMixin

from .models import Item


class ItemSerializer(serializers.ModelSerializer, EagerLoadingMixin):
    class Meta:
        model = Item
        fields = (
            "id",
            "label",
            "quantity",
            "package",
        )
        read_only_fields = (
            "id",
            "label",
            "quantity",
            "package",
        )
