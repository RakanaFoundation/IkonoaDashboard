from django.db import models
from pos.models.cabangmodels import Cabang

class NotaCabang(models.Model):
    cabang = models.ForeignKey(
        Cabang,
        unique=False,
        on_delete=models.DO_NOTHING
    )
    notanumber = models.IntegerField(default=1)

    