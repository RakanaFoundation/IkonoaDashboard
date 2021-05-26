from pos.models.departmentmodels import DeptGrup
from rest_framework import serializers

class DeptGrupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DeptGrup
        fields = [
            'code',
            'name'
        ]