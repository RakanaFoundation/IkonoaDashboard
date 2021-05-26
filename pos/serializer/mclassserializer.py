from rest_framework import serializers
from pos.models.mclassmodel import Mclass
from pos.serializer.departmentserializer import DeptSerializer

class MclassSerializer(serializers.ModelSerializer):
    dept = DeptSerializer(many=False)

    class Meta:
        model = Mclass
        fields = [
            'code',
            'name',
            'dept'
        ]