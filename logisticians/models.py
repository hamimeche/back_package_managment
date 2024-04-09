from django.db import models

class Logistician(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
