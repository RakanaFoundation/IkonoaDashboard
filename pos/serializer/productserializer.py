from pos.models.models import Product
from pos.serializer.departmentserializer import DeptSerializer
from pos.serializer.mclassserializer import MclassSerializer
from pos.serializer.categoryserializer import *
from rest_framework import serializers
from pos.serializer.promotionserializers import PromotionSerializer

class ProductSerializer(serializers.ModelSerializer):
    dept = DeptSerializer(many=False)
    mclass = MclassSerializer(many=False)
    promotions = PromotionSerializer(many=False)
    mainCategory = MainCategorySerializer(many=False)
    subCategoryOne = SubCategoryOneSerializer(many=False)
    subCategoryTwo = SubCategoryTwoSerializer(many=False)

    class Meta:
        model = Product
        fields = [
            'id',
            'sku',
            'barcode',
            'description',
            'hargaBeli',
            'hargaJual',
            'hargaJual2',
            'hargaJual3',
            'hargaBeliBesar',
            'hpp',
            'dept',
            'mclass',
            'returnable',
            'promotions',
            'mainCategory',
            'subCategoryOne',
            'subCategoryTwo'
        ]