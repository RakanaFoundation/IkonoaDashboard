from django.db import models

class Cabang(models.Model):
    address = models.CharField(max_length=254)
    phone = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True)
    name = models.CharField(max_length=100)