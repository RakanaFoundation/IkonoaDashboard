from rest_framework import serializers
from .financemodels import Payment, SalesTransaction
from .salesmodels import ProductSalesTransaction
from .cabangmodels import Cabang
from .usermodels import Employee
from .models import Product
from .promotionmodels import Promotion
from .userserializers import EmployeeSerializers
from .cabangserializers import CabangSerializer
from .serializers import ProductSerializer
from .promotionserializers import PromotionSerializer
import json

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
            'promotion'
            ]

    def get_product_sales(self, salesTransaction):
        return GetProductSalesSerializers(
            ProductSalesTransaction.objects.filter(salesTransaction = salesTransaction), many=True).data

class CreateSalesTransactionSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=False)
    productSales = CreateProductSalesSerializers(many=True)
    promotion = serializers.CharField()

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

        promotion = Promotion.objects.get(name=promoData)
        
        salesTransaction = SalesTransaction.objects.create(
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



