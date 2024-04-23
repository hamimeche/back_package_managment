from rest_framework import serializers

from .models import Package

from items.models import Item


class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Package

        fields = [
            "code",
            "weight",
            "delivery_date",
            "status",
        ]


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item

        fields = [
            "label",
            "quantity",
        ]
