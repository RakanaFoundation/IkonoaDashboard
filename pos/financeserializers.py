from rest_framework import serializers
from .financemodels import Payment, SalesTransaction
from .salesmodels import ProductSalesTransaction
from .cabangmodels import Cabang
from .usermodels import Employee
from .models import Product
from .promotionmodels import Promotion
from .notamodels import NotaCabang
from .userserializers import EmployeeSerializers
from .cabangserializers import CabangSerializer
from .serializers import ProductSerializer
from .promotionserializers import PromotionSerializer
from datetime import datetime
from django.db.models import F
from pos.inventorysignals import incrementCabangInventory
import json

class SpendingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        
        fields = [
            'id', 
            'amount', 
            'detail', 
            'date', 
            'refund', 
            'paymethod',
            'expiryDate',
            'paymethod'
            ]


class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = [
            'id', 
            'amount', 
            'detail', 
            'date', 
            'refund', 
            'paymethod',
            'expiryDate',
            'paymethod'
            ]

    def create(self, validated_data):
        return Payment.objects.create(**validated_data)

class GetProductSalesSerializers(serializers.ModelSerializer):
    product = ProductSerializer(many=False)
    salesTransaction = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    
    class Meta:
        model = ProductSalesTransaction
        fields = [
            'product',
            'salesTransaction',
            'amount',
            'quantity'
        ]

class CreateProductSalesSerializers(serializers.ModelSerializer):
    product = serializers.IntegerField(read_only=False)

    class Meta:
        model = ProductSalesTransaction
        fields = [
            'product',
            'amount',
            'quantity'
        ]

class GetSalesTransactionSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=False)
    productSales = serializers.SerializerMethodField('get_product_sales')
    promotion = PromotionSerializer(many=False)

    class Meta:
            model = SalesTransaction
            fields = [
            'id',
            'sales_id', 
            'date', 
            'amount', 
            'comment', 
            'employee',
            'cabang',
            'payment',
            'detail',
            'productSales',
            'promotion',
            'refund'
            ]

    def get_product_sales(self, salesTransaction):
        return GetProductSalesSerializers(
            ProductSalesTransaction.objects.filter(salesTransaction = salesTransaction), many=True).data

def doCreateSalesTransaction(validated_data):
    amount = validated_data.get('amount')
    detail = validated_data.get('detail')
    comment = validated_data.get('comment')

    employeeData = validated_data.get('employee')
    employee = Employee.objects.get(id=employeeData.id)
    
    cabangData = validated_data.get('cabang')
    cabang = Cabang.objects.get(id=cabangData.id)
    
    paymentData = validated_data.get('payment')

    payment = Payment.objects.create(**paymentData)

    promoData = validated_data.get('promotion')

    promotion = None
    if promoData is not None:
        promotion = Promotion.objects.get(name=promoData)
        
    try:
        notaCabang = NotaCabang.objects.get(cabang=cabang)
    except NotaCabang.DoesNotExist:
        notaCabang = NotaCabang.objects.create(
            cabang=cabang
        )

    salesNumber = str(cabang.code) + str(notaCabang.notanumber) + str(datetime.today().strftime('%d%m%y'))
    NotaCabang.objects.filter(cabang=cabang).update(notanumber=F('notanumber') + 1) 
    
    salesTransaction = SalesTransaction.objects.create(
        sales_id = salesNumber,
        amount = amount,
        detail = detail,
        comment = comment,
        employee = employee,
        payment = payment,
        cabang = cabang,
        promotion = promotion
    )

    productSalesData = validated_data.get('productSales')
    for productSales in productSalesData:
        productId = productSales.get("product")
        product = Product.objects.get(id=productId)
        ProductSalesTransaction.objects.create(
            product=product,
            salesTransaction=salesTransaction,
            amount = productSales.get("amount"),
            quantity = productSales.get("quantity")
        )
    return validated_data

class CreateSalesTransactionSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=False)
    productSales = CreateProductSalesSerializers(many=True)
    promotion = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = SalesTransaction
        fields = [
        'sales_id', 
        'date', 
        'amount', 
        'comment', 
        'employee',
        'cabang',
        'payment',
        'detail', 
        'productSales',
        'promotion'
        ]

    def create(self, validated_data):
        return doCreateSalesTransaction(validated_data)
        

class CreateReturSalesTransactionSerializer(serializers.ModelSerializer):
    retur_sales_id = serializers.CharField(required=True)
    payment = PaymentSerializer(many=False)
    productSales = CreateProductSalesSerializers(many=True)
    promotion = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = SalesTransaction
        fields = [
        'retur_sales_id', 
        'date', 
        'amount', 
        'comment', 
        'employee',
        'cabang',
        'payment',
        'detail', 
        'productSales',
        'promotion'
        ]

    def create(self, validated_data):
        returSalesId = validated_data.get("retur_sales_id")
        oldSales = SalesTransaction.objects.get(sales_id=returSalesId)
        oldSales.refund = True
        oldSales.save()

        productSales = ProductSalesTransaction.objects.filter(salesTransaction=oldSales)
        if productSales:
            for prodSale in productSales:
                cabang = prodSale.salesTransaction.cabang
                incrementCabangInventory(cabang, prodSale.product, prodSale.quantity)

        oldPaymentToRetur = oldSales.payment
        oldPaymentToRetur.refund = True
        oldPaymentToRetur.save()

        return doCreateSalesTransaction(validated_data)





