from django.db import models
from pos.models.cabangmodels import Cabang
from pos.models.usermodels import Employee

class CabangSpv(models.Model):
    cabang = models.ForeignKey(
        Cabang,
        unique=False,
        on_delete=models.CASCADE
    )

    spv = models.ForeignKey(
        Employee,
        unique=False,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return str()