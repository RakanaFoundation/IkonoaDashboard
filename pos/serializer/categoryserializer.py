from rest_framework import serializers
from pos.models.models import MainCategory, SubCategoryOne, SubCategoryTwo

class MainCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MainCategory
        fields = [
            'description'
        ]

class SubCategoryOneSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategoryOne
        fields = [
            'description'
        ]

class SubCategoryTwoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategoryTwo
        fields = [
            'description'
        ]