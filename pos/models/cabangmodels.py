from django.db import models
from pos.models.districtmodels import District

class Cabang(models.Model):
    address = models.CharField(max_length=254)
    phone = models.CharField(max_length=50)
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, default = '')
    district = models.ForeignKey(
        District,
        unique = False,
        on_delete = models.DO_NOTHING
    )

    def __str__(self):
        return self.name



    