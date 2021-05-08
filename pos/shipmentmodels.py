from django.db import models
from pos.financemodels import SalesTransaction
from pos.cabangmodels import Cabang
from pos.models import Product
import datetime

REJECT = 'REJECT'
APPROVE = 'APPROVE'
PENDING = 'PENDING'
RECEIVED = 'RECEIVED'
INSHIPMENT = 'IN_SHIPMENT'

STATUS_CHOICES_LIST = [
    REJECT,
    APPROVE,
    PENDING
]

STATUS_ORDER_SHIPMENT = [
    (REJECT, 'Rejected'),
    (INSHIPMENT, 'Inshipment'),
    (RECEIVED, 'Received')
]

STATUS_CHOICES = [
    (REJECT, 'Rejected'),
    (APPROVE, 'Approved'),
    (PENDING, 'Pending')
]

class Order(models.Model):
    cabang = models.ForeignKey(
        Cabang,
        unique=False,
        on_delete=models.DO_NOTHING
    )

    createdDate = models.DateTimeField(
        auto_now_add=True)

class OrderRequest(models.Model):
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

    status = models.CharField(
        max_length=20,
        choices=STATUS_ORDER_SHIPMENT,
        default=INSHIPMENT,
    )

    detail = models.CharField(
            max_length=200,
            null=True,
            blank=True
            )
            
    date = models.DateTimeField(auto_now_add=True)

class OrderReturn(models.Model):
    order = models.ForeignKey(
        Order,
        unique=False,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_ORDER_SHIPMENT,
        default=INSHIPMENT,
    )

    detail = models.CharField(
        max_length=200,
        null=True,
        blank=True)

    date = models.DateTimeField(auto_now_add=True)

class ProductOrder(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        unique=False
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        unique=False
    )

    quantity = models.IntegerField(default=1)
    detail = models.CharField(max_length=200, blank=True, null=True)


