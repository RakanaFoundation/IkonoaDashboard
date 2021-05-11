from django.db import models
from pos.models.models import Product
from pos.models.cabangmodels import Cabang

class Inventory(models.Model):
    cabang = models.OneToOneField(
        Cabang,
        on_delete=models.DO_NOTHING
    )

    detail = models.CharField(
        max_length=200, 
        blank=True, 
        null=True)
    
class PusatProductInventory(models.Model):
    product = models.ForeignKey(
        Product,
        unique=False,
        on_delete=models.DO_NOTHING
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    reminderStockAt = models.PositiveIntegerField(
        default=0
    )

class ProductInventory(models.Model):
    inventory = models.ForeignKey(
        Inventory,
        unique=False,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        unique=False,
        on_delete=models.DO_NOTHING
    )

    stock = models.PositiveIntegerField(
        default=0
    )

    reminderStockAt = models.PositiveIntegerField(
        default=0
    )