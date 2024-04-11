from rest_framework import serializers

from core.common import EagerLoadingMixin
from items.serializers import ItemSerializer

from .models import Package


class PackageShortSerializer(serializers.ModelSerializer, EagerLoadingMixin):
    class Meta:
        model = Package
        fields = (
            "id",
            "code",
            "weight",
            "delivery_date",
            "status",
            "logistician",
        )
        read_only_fields = (
            "id",
            "code",
            "weight",
            "delivery_date",
            "logistician",
        )


class PackageFullSerializer(serializers.ModelSerializer, EagerLoadingMixin):
    _PREFETCH_RELATED_FIELDS = ("items",)

    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = (
            "id",
            "code",
            "weight",
            "delivery_date",
            "status",
            "logistician",
            "items",
        )
        read_only_fields = (
            "id",
            "code",
            "weight",
            "delivery_date",
            "logistician",
        )
