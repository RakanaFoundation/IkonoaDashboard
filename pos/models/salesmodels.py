from django.db import models
from pos.models.financemodels import SalesTransaction
from pos.models.models import Product


class ProductSalesTransaction(models.Model):
    product = models.ForeignKey(
        Product,
        unique=False,
        on_delete=models.DO_NOTHING
    )

    salesTransaction = models.ForeignKey(
        SalesTransaction,
        related_name='productSales',
        unique=False,
        on_delete=models.CASCADE    
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField()

    