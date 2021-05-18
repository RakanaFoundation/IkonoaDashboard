from rest_framework import serializers
from pos.models.cabangmodels import Cabang
from pos.models.districtmodels import District

class DistrictSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = District
        fields = [
            'name'
        ]

class CabangSerializer(serializers.ModelSerializer):
    dist = DistrictSerializer(many=False)

    class Meta:
        model = Cabang
        fields = [ 
            'id', 
            'address', 
            'phone', 
            'email', 
            'name',
            'code',
            'dist'
            ]