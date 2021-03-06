from django.db import models
from django.contrib.auth.models import User
from pos.models.cabangmodels import Cabang

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cabang = models.ForeignKey(
        Cabang,
        unique=False,
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.user