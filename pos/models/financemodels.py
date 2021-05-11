from django.db import models
import datetime
from pos.models.cabangmodels import Cabang
from pos.models.usermodels import Employee
import datetime
from pos.models.promotionmodels import Promotion

CASH = 'CASH'
GIRO = 'GIRO'
CARD = 'CARD'

PAYMENT_CHOICES = [
    (CASH, 'Cash'),
    (GIRO, 'Giro'),
    (CARD, 'Card'),
]

class Spending(models.Model):
    paymethod = models.CharField(
        max_length=4,
        choices=PAYMENT_CHOICES,
        default=CASH,
    )

    expiryDate = models.DateTimeField(
        auto_now_add=False, 
        null=True, 
        blank=True
        )

    amount = models.DecimalField(max_digits=15, decimal_places=2)
    detail = models.CharField(max_length=200, null=True,
        blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount) + str(self.detail)

class Payment(models.Model):
    paymethod = models.CharField(
        max_length=4,
        choices=PAYMENT_CHOICES,
        default=CASH,
    )

    expiryDate = models.DateTimeField(
        auto_now_add=False, 
        null=True, 
        blank=True
        )

    amount = models.DecimalField(max_digits=15, decimal_places=2)
    detail = models.CharField(max_length=200, null=True,
        blank=True)
    date = models.DateTimeField(
        auto_now_add=True
    )
    refund = models.BooleanField(default=False)

    def __str__(self):
        return str(self.amount) + str(self.detail)

class SalesTransaction(models.Model):
    sales_id = models.CharField(max_length = 200, default = '')
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    detail = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    refund = models.BooleanField(default=False)
    employee = models.ForeignKey(
        Employee,
        unique=False,
        on_delete=models.DO_NOTHING
    )
    payment = models.ForeignKey(
        Payment,
        unique=False,
        on_delete=models.CASCADE
    )
    cabang = models.ForeignKey(
        Cabang,
        unique=False,
        on_delete=models.DO_NOTHING
    )
    promotion = models.ForeignKey(
        Promotion,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        unique=False
    )

    
