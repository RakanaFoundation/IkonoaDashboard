from django.db import models
from pos.financemodels import SalesTransaction
from pos.cabangmodels import Cabang
import datetime

REJECTED = 'REJECT'
APPROVED = 'APPROVE'
PENDING = 'PENDING'

STATUS_CHOICES = [
    (REJECTED, 'Rejected'),
    (APPROVED, 'Approved'),
    (PENDING, 'Pending')
]

class Order(models.Model):
    createdDate = models.DateTimeField(
        auto_now_add=True)

class OrderRequest(models.Model):
    cabang = models.ForeignKey(
        Cabang,
        unique=False,
        on_delete=models.DO_NOTHING
    )

    order = models.ForeignKey(
        Order,
        unique=False,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    detail = models.CharField(
        max_length=200,
        null=True,
        blank=True)

class OrderReceived(models.Model):
    order = models.ForeignKey(
        Order,
        unique=False,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=PENDING,
    )

    detail = models.CharField(
        max_length=200,
        null=True,
        blank=True)

class Shipment(models.Model):
    courier = models.CharField(max_length=200)
    trackingId = models.CharField(max_length=200)
    detail = models.CharField(
        max_length=200,
        null=True,
        blank=True
        )

class OrderSent(models.Model):
    order = models.ForeignKey(
        Order,
        unique=False,
        on_delete=models.CASCADE
    )

    shipment = models.ForeignKey(
        Shipment,
        unique=False,
        on_delete=models.DO_NOTHING
    )

class OrderReturn(models.Model):
    cabang = models.ForeignKey(
        Cabang,
        unique=False,
        on_delete=models.DO_NOTHING
    )
    
    order = models.ForeignKey(
        Order,
        unique=False,
        on_delete=models.CASCADE
    )

    shipment = models.ForeignKey(
        Shipment,
        unique=False,
        on_delete=models.DO_NOTHING
    )

    salesTransaction = models.ForeignKey(
        SalesTransaction,
        unique=False,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )

    detail = models.CharField(
        max_length=200,
        null=True,
        blank=True)

    date = models.DateTimeField(auto_now_add=True)


