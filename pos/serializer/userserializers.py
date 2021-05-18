from rest_framework import serializers
from pos.models.usermodels import Employee
from pos.serializer.cabangserializers import CabangSerializer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            'username', 
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'date_joined',
            'is_superuser',
            'email'
            ]

class EmployeeSerializers(serializers.ModelSerializer):
    cabang = CabangSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta: 
        model = Employee
        fields = ['id', 'user', 'cabang']