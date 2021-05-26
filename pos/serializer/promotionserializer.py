from pos.models.promotionmodels import Promotion
from rest_framework import serializers

class PromotionSerializer(serializers.ModelSerializer):

    class meta:
        model = Promotion
        fields = [
            'name',
            'description',
            'dateFrom',
            'dateTo',
            'created',
            'percentage'
        ]