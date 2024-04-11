from django.db import models

from logisticians.models import Logistician

from .constants import PACKAGE_STATUS


class Package(models.Model):
    code = models.CharField(max_length=100)
    weight = models.FloatField()
    delivery_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=PACKAGE_STATUS, max_length=100)
    logistician = models.ForeignKey(Logistician, on_delete=models.CASCADE)

    def __str__(self):
        return self.code
