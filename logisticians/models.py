from django.db import models
from django.contrib.auth.models import User


class Logistician(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LogisticianUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    logistician_infos = models.OneToOneField(
        Logistician, on_delete=models.CASCADE, primary_key=True
    )
