from django.db import models
import datetime
from pos.cabangmodels import Cabang
from pos.usermodels import Employee
import datetime

class PaymentMethod(models.Model):
    CASH = 'CASH'
    GIRO = 'GIRO'
    CARD = 'CARD'
    
    PAYMENT_CHOICES = [
        (CASH, 'Cash'),
        (GIRO, 'Giro'),
        (CARD, 'Card'),
    ]

    detail = models.CharField(
        max_length=4,
        choices=PAYMENT_CHOICES,
        default=CASH,
    )
    expiryDate = models.DateTimeField(
        auto_now_add=False, 
        null=True, 
        blank=True,
        default=datetime.date.today
        )

    def __str__(self):
        return self.detail

class Spending(models.Model):
    paymentMethod = models.ForeignKey(
        PaymentMethod,
        on_delete=models.DO_NOTHING,
        unique=False
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    detail = models.CharField(max_length=200, null=True,
        blank=True)
    date = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    paymentMethod = models.ForeignKey(
        PaymentMethod,
        on_delete=models.DO_NOTHING,
        unique=False
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    detail = models.CharField(max_length=200, null=True,
        blank=True)
    date = models.DateTimeField(
        auto_now_add=True
    )
    refund = models.BooleanField(default=False)

def increment_sales_number():
    last_sales = SalesTransaction.objects.all().order_by('id').last()
    if not last_sales:
        return 'STR' +str(datetime.date.today().year) + str(datetime.date.today().month).zfill(2) + '0000'
    
    sales_id = last_sales.sales_id
    sales_int = int(sales_id[9:13])
    new_sales_int = sales_int + 1
    new_sales_id = 'STR' + str(str(datetime.date.today().year)) 
    + str(datetime.date.today().month).zfill(2) 
    + str(new_sales_int).zfill(4)
    return new_sales_id

class SalesTransaction(models.Model):
    sales_id = models.CharField(max_length = 200, default = increment_sales_number, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    detail = models.CharField(max_length=200, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
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

class ProductSalesTransaction(models.Model):
    product = models.ForeignKey(
        Employee,
        unique=False,
        on_delete=models.DO_NOTHING
    )

    salesTransaction = models.ForeignKey(
        SalesTransaction,
        unique=False,
        on_delete=models.CASCADE    
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    quantity = models.IntegerField()

    
