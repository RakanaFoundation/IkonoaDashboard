from django.db import models
from pos.models.districtmodels import District

class Cabang(models.Model):
    dist = models.ForeignKey(
        District,
        on_delete = models.DO_NOTHING
    )

    address = models.CharField(max_length=254)
    phone = models.CharField(max_length=50,
        null=True,
        blank=True)
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, default = '')
    
    def __str__(self):
        return self.name



    