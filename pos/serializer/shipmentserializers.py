from rest_framework import serializers
from pos.models.models import Faktur, Supplier, ProductFaktur, Product
from pos.models.financemodels import Spending
from pos.serializer.financeserializers import SpendingSerializer

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = [
            'address', 
            'phone', 
            'email', 
            'name'
            ]

class CreateProductFakturSerializer(serializers.ModelSerializer):
    product = serializers.IntegerField(read_only=False)
    
    class Meta:
        model = ProductFaktur
        fields = [
            'product',
            'detail',
            'quantity'
        ]

class CreateFakturSerializer(serializers.ModelSerializer):
    spending = SpendingSerializer()
    supplier = serializers.IntegerField(read_only=False)
    productFaktur = CreateProductFakturSerializer(many=True)

    class Meta:
        model = Faktur
        fields = [
            'supplier',
            'spending',
            'productFaktur'
            ]

    def create(self, validated_data):
        
        supplierData = validated_data.get('supplier')
        supplier = Supplier.objects.get(id=supplierData)

        spendingData = validated_data.get('spending')
        spending = Spending.objects.create(**spendingData)

        faktur = Faktur.objects.create(
            supplier = supplier,
            spending = spending
        )

        productFakturData = validated_data.get('productFaktur')
        for productFaktur in productFakturData:
            productId = productFaktur.get("product")
            product = Product.objects.get(id=productId)
            ProductFaktur.objects.create(
                product = product,
                faktur = faktur,
                detail = productFaktur.get("detail"),
                quantity = productFaktur.get("quantity")
            )

        return validated_data
