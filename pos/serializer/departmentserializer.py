from pos.models.departmentmodels import Dept
from pos.serializer.departmentgroupserializer import DeptGrupSerializer
from rest_framework import serializers

class DeptSerializer(serializers.ModelSerializer):
    deptGroup = DeptGrupSerializer( many = False )
    
    class Meta:
        model = Dept
        fields = [
            'code',
            'name',
            'deptGroup'
        ]