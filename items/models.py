from django.db import models

from packages.models import Package


class Item(models.Model):
    label = models.CharField(max_length=100)
    quantity = models.IntegerField()
    package = models.ForeignKey(Package, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom