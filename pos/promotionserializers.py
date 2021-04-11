from rest_framework import serializers
from pos.promotionmodels import Promotion

class PromotionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotion
        fields = [
            'name',
            'description',
            'dateFrom',
            'dateTo',
            'created',
            'percentage'
        ]