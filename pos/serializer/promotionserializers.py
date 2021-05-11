from rest_framework import serializers
from pos.models.promotionmodels import Promotion

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