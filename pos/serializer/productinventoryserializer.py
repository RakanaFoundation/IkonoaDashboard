from rest_framework import serializers
from pos.models.inventorymodels import ProductInventory
from pos.serializer.productserializer import ProductSerializer

class ProductInventorySerilizer(serializers.ModelSerializer):
    product = ProductSerializer(many=False)

    class Meta:
        model = ProductInventory
        fields = [
            'inventory',
            'product',
            'stock',
            'reminderStockAt'
        ]