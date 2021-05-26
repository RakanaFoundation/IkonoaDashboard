from pos.models.inventorymodels import ProductInventory
from rest_framework import serializers

class ProductInventory(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductInventory
        fields = (
            'id', 
            'description', 
            'hargaBeli', 
            'hargaJual', 
            'barcode', 
            'returnable'
            )