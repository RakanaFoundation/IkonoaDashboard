from django.db import models
from pos.models.models import Supplier
from pos.models.buyermodel import Buyer
from pos.models.mclassmodel import Mclass

class Merk(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=50)
    mclass = models.ForeignKey(Mclass, on_delete=models.DO_NOTHING)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    buyer = models.ForeignKey(Buyer, on_delete=models.DO_NOTHING)
    margin = models.IntegerField()

    def __str__(self):
        return self.code